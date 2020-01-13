from django.shortcuts import render, redirect, reverse
from accounts.forms import UserRegistrationForm, UserLoginForm, ProfileAddressForm
from accounts.models import Profile
from django.contrib import messages
from .contexts import cart_contents
from accounts import views

def view_cart(request):

    if request.user.is_authenticated:

        if request.session.get('amended'):
            print("amended")
            del request.session['amended']
        
        try:
            current_user = request.user
            user = Profile.objects.get(username=current_user)
            profile_form = ProfileAddressForm(instance=user)
        
        except:
            profile_form = ProfileAddressForm()

        if 'checkout' in request.POST:
            if profile_form.is_valid():
                return render(request, 'shipping.html')

            else:
                messages.error(request, "Keep an eye on your mana! Something went wrong with that form.")
                return redirect(reverse('view_cart'))

        else:
            return render(request, 'cart.html', {'profile_form': profile_form})

    else:
        cart_access = True
        request.session['cart_access'] = cart_access
        return redirect(reverse('logreg'))


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart."""
    quantity = request.POST.get('quantity')

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    str_id = str(id)
    if str_id in cart:
        cart[id] = int(cart[id]) + int(quantity) 

    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def amend_cart(request, id):
    """Adjust the quantity of the specified product to the specified amount."""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    print(cart)

    if quantity > 0:
        cart = cart[id] = quantity
    else:
        cart = cart.pop(str(id))    
    
    request.session['cart'] = cart

    amended = True
    request.session['amended'] = amended
    return redirect(reverse('view_cart'))