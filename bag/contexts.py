from decimal import Decimal
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    # Create a copy of the bag dictionary to avoid modifying it while iterating
    bag_copy = bag.copy()

    for item_id, item_data in bag_copy.items():
        try:
            # Try to get the product from the database
            if isinstance(item_data, int):
                product = Product.objects.get(pk=item_id)
                total += item_data * product.price
                product_count += item_data
                bag_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                })
            else:
                product = Product.objects.get(pk=item_id)
                for size, quantity in item_data['items_by_size'].items():
                    total += quantity * product.price
                    product_count += quantity
                    bag_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                    })

        except ObjectDoesNotExist:
            # If the product doesn't exist, remove it from the bag
            del bag[item_id]
            continue  # Continue with the next item in the loop

    # Save the modified bag in the session
    request.session['bag'] = bag

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
