from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    # Get all products
    all_products = Product.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                all_products = all_products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            all_products = all_products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            all_products = all_products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            all_products = all_products.filter(queries)

    # Create a Paginator instance with a specified number of products per page
    paginator = Paginator(all_products, 48)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    # Get the Page object for the current page
    products = paginator.get_page(page)

    current_sorting = f'{sort}_{direction}'
    current_sort = sort
    current_direction = direction

    context = {
        'all_products': all_products,
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'current_sort': current_sort,
        'current_direction': current_direction,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individul product details and handle reviews """

    product = get_object_or_404(Product, pk=product_id)

    # Fetch all reviews associated with the product
    reviews = Review.objects.filter(product=product).filter(approved=True)

    if request.method == 'POST':
        # Handle form submission for creating a new review
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.info(request, 'Review pended for approval')
            return redirect('product_detail', product_id=product_id)
        else:
            messages.error(
                request, 'Failed to add review. Please check the form.')

    else:
        form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,  # Pass the reviews to the template
        'form': form,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.info(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    # Check if the request method is POST (confirmation form submission)
    if request.method == 'POST':

        # Check if the product is in the bag and remove it if it is
        bag = request.session.get('bag', {})
        if str(product_id) in bag:
            del bag[str(product_id)]
            request.session['bag'] = bag

        # Delete the product and redirect to a success page
        product.delete()
        messages.info(request, 'Product deleted!')
        return redirect(reverse('products'))

    # If it's a GET request, render the confirmation page
    template = 'products/delete_product.html'
    context = {
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user.is_superuser:
        review.delete()
        return redirect('review_list')
    if request.user == review.user:
        review.delete()
        return redirect('product_detail', product_id=review.product.id)
    else:
        messages.error(request, 'Sorry, only the reviewer or a superuser can do that')
        return redirect('home')


@user_passes_test(lambda u: u.is_staff)  # Ensure only staff can access
def review_list(request):
    reviews = Review.objects.filter(approved=False).order_by('created_at')
    return render(request, 'products/reviews_list.html', {'reviews': reviews})


@user_passes_test(lambda u: u.is_staff)  # Ensure only staff can access
def approve_review(request, review_id):
    if not request.user.is_staff:
        raise PermissionDenied
    try:
        review = Review.objects.get(pk=review_id)
        review.approved = True
        review.save()
        messages.info(request, 'Review approved')
    except Review.DoesNotExist:
        pass
    return redirect('review_list')  # Redirect to a page that lists reviews
