from django.shortcuts import render, redirect, reverse
from accounts.forms import UserRegistrationForm, UserLoginForm
from accounts.views import logreg

def view_cart(request):

    if request.user.is_authenticated:
        return render(request, 'cart.html')

    else:
        return redirect(reverse('logreg'))


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart."""

    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))
