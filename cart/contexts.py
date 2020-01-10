from django.shortcuts import get_object_or_404
from items.models import Item


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    print(cart)

    if cart != {}:
    
        for id, quantity in cart.items():
            product = get_object_or_404(Item, pk=id)
            quantity = int(quantity)
            total += quantity * product.price
            product_count += quantity
            cart_items.append({'id': id, 'quantity': quantity, 'product': product})
    
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}