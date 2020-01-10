from django.shortcuts import render, redirect, reverse
from accounts.forms import UserRegistrationForm, UserLoginForm

def view_cart(request):

    if request.user.is_authenticated:
        return render(request, 'cart.html')

    else:
        register_form = UserRegistrationForm()
        login_form = UserLoginForm()
        cart = True
        request.session['cart'] = cart
        args = {'register_form': register_form, 'login_form': login_form}

        return render(request, 'logreg.html', args)

def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart."""

    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))
