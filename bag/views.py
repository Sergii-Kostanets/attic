from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404
)
from django.contrib import messages
from products.models import Product
from .contexts import bag_contents
from django.conf import settings


def view_bag(request):
    """ A view that renders the bag contents page """

    context = bag_contents(request)

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    current_bag = bag_contents(request)
    grand_total = current_bag['grand_total']

    # Check if adding this item will exceed the limit
    if grand_total + (quantity * product.price) > settings.MAX_ORDER_TOTAL:
        messages.error(request, 'Adding this item will exceed \
            the maximum order total')
        return redirect(reverse('view_bag'))

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                # Check if adding the quantity exceeds 99
                if bag[item_id]['items_by_size'][size] + quantity > 99:
                    messages.error(request, 'You can only add up to 99 \
                        of the same item')
                else:
                    bag[item_id]['items_by_size'][size] += quantity
                    messages.success(
                        request,
                        f'Updated {product.name} (size {size}) quantity \
                            to {bag[item_id]["items_by_size"][size]}')
            else:
                # Check if adding the quantity exceeds 99
                if quantity > 99:
                    messages.error(request, 'You can only add up to 99 \
                        of the same item.')
                else:
                    bag[item_id]['items_by_size'][size] = quantity
                    messages.success(request, f'Added {product.name} \
                        (size {size}) to your bag')
        else:
            # Check if adding the quantity exceeds 99
            if quantity > 99:
                messages.error(request, 'You can only add up to 99 \
                    of the same item.')
            else:
                bag[item_id] = {'items_by_size': {size: quantity}}
                messages.success(request, f'Added {product.name} \
                    (size {size}) to your bag')
    else:
        if item_id in list(bag.keys()):
            # Check if adding the quantity exceeds 99
            if bag[item_id] + quantity > 99:
                messages.error(request, 'You can only add up to 99 \
                    of the same item.')
            else:
                bag[item_id] += quantity
                messages.success(request, f'Updated {product.name} quantity \
                    to {bag[item_id]}')
        else:
            # Check if adding the quantity exceeds 99
            if quantity > 99:
                messages.error(request, 'You can only add up to 99 \
                    of the same item.')
            else:
                bag[item_id] = quantity
                messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    if quantity < 1 or quantity > 99:
        messages.error(request, 'Quantity must be between 1 and 99')
        return redirect(reverse('view_bag'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated {product.name} (size {size}) quantity \
                to {bag[item_id]["items_by_size"][size]}'
            )
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size'][size]:
                bag.pop(item_id)
            messages.success(request, f'Removed {product.name} \
                (size {size}) from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity \
                to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name} (size {size}) from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
