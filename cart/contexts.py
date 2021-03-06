from django.shortcuts import get_object_or_404
from items.models import Item
import decimal


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    if cart != {}:
    
        for id, quantity in cart.items():
            product = get_object_or_404(Item, pk=id)
            quantity = int(quantity)
            total += quantity * product.price + decimal.Decimal('7.50')
            product_count += quantity
            cart_items.append(
                {'id': id,
                'quantity': quantity,
                'product': product,
                'total': total
                }
            )

    return {
        'cart_items': cart_items, 'total': total, 'product_count': product_count}  