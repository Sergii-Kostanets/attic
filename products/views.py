from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.core.paginator import Paginator


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
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            all_products = all_products.filter(queries)

    # Create a Paginator instance with a specified number of products per page
    paginator = Paginator(all_products, 48)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    # Get the Page object for the current page
    products = paginator.get_page(page)

    # current_sorting = f'{sort}_{direction}'
    current_sorting = sort
    current_direction = direction

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'current_direction': current_direction,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individul product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
