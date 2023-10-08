from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WishlistItem
from products.models import Product
from django.contrib import messages


@login_required
def view_wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(
        request, 'wishlist/wishlist.html', {'wishlist_items': wishlist_items})


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # Check if the product is already in the user's wishlist
    wishlist_item_query = WishlistItem.objects.filter(
        user=request.user, product=product)
    if wishlist_item_query.exists():
        messages.info(
            request, f'You already have {product.name} in the wishlist')
        return redirect('product_detail', product_id=product_id)

    # If the product is not in the wishlist, add it
    WishlistItem.objects.create(user=request.user, product=product)
    messages.info(
        request, f'{product.name} successfuly added to the wishlist')
    return redirect('product_detail', product_id=product_id)


@login_required
def remove_from_wishlist(request, wishlist_item_id):
    wishlist_item = get_object_or_404(
        WishlistItem, pk=wishlist_item_id, user=request.user)
    wishlist_item.delete()
    return redirect('view_wishlist')
