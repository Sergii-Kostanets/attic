from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    # Get all products
    all_products = Product.objects.all()

    # Create a Paginator instance with a specified number of products per page
    paginator = Paginator(all_products, 48)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    # Get the Page object for the current page
    products = paginator.get_page(page)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individul product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
