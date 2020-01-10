from django.shortcuts import render, redirect, reverse
from accounts.forms import UserRegistrationForm, UserLoginForm, ProfileAddressForm
from accounts.models import Profile
from django.contrib import messages
from accounts import views

def view_cart(request):

    if request.user.is_authenticated:
        print("authenticated")
        try:
            current_user = request.user
            user = Profile.objects.get(username=current_user)
            profile_form = ProfileAddressForm(instance=user)
            return render(request, 'cart.html', {'profile_form': profile_form})
        
        except:
            profile_form = ProfileAddressForm()
            return render(request, 'cart.html', {'profile_form': profile_form})

    else:
        return redirect(reverse('logreg'))


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart."""
    quantity = request.POST.get('quantity')

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    str_id = str(id)
    if str_id in cart:
        print("exists")

    else:
        print("doesn't exist")

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
