from django.shortcuts import render, redirect, reverse
from accounts.forms import UserRegistrationForm, UserLoginForm, ProfileAddressForm
from django.shortcuts import get_object_or_404
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .contexts import cart_contents
from django.conf import settings
from items.models import Item
from .models import Order
from .forms import MakePaymentForm
from accounts import views
import stripe
import os
import datetime

stripe.api_key = settings.STRIPE_SECRET
print(stripe.api_key)

def view_cart(request):

    if request.user.is_authenticated:

        if request.session.get('amended'):
            del request.session['amended']
        
        try:
            current_user = request.user
            user = Profile.objects.get(username=current_user)
            profile_form = ProfileAddressForm(instance=user)
        
        except:
            profile_form = ProfileAddressForm()

        if 'shipping' in request.POST:

            profile_form = ProfileAddressForm(request.POST)
            if profile_form.is_valid():
                user = request.user
                profile = profile_form.cleaned_data
                obj, created = Profile.objects.update_or_create(username=user, defaults=profile)
                return redirect(reverse('view_payment'))

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

@login_required
def amend_cart(request, id):
    """Adjust the quantity of the specified product to the specified amount."""

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(str(id))    
    
    amended = True
    request.session['amended'] = amended

    if request.session.get('shipping'):
        del request.session['shipping']
        return redirect(reverse('view_payment'))

    else:    
        return redirect(reverse('view_cart'))


@login_required
def view_payment(request):

    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    profile_form = ProfileAddressForm(instance=profile)

    payment_form = MakePaymentForm()

    payment = True

    return render(request, 'payment.html', {'profile_form': profile_form, 'payment_form': payment_form, 'profile': profile, 'payment': payment})


def payment(request):
    
    payment_form = MakePaymentForm(request.POST)
    if payment_form.is_valid():

        print("is valid")

        # for id, quantity in cart.items():
        #     product = get_object_or_404(Item, pk=id)
        #     quantity = int(quantity)
        #     total += float(quantity * product.price)
        #     product_count += quantity
        #     cart_items.append({'id': id, 'quantity': product_count, 'product': product})
        #     order = Order.objects.create(user=request.user, quantity=quantity)
        #     order.products.add(id)
        #     order.save()

        #  try:
    #     customer = stripe.Charge.create(
    #     amount=int(total * 100),
    #     currency="EUR",
    #     description=request.user.email,
    #     card=payment_form.cleaned_data['stripe_id']
    #         )

    #     except stripe.error.CardError:
    #         messages.error(request, "Your card was declined!")
            
    #     if customer.paid:
    #         messages.error(request, "You have successfully paid")
    #         request.session['cart'] = {}
    #         return redirect(reverse('view_confirm'))
    #     else:
    #         messages.error(request, "Unable to take payment")
    #         return redirect(reverse('view_payment'))

    # else:
    #     messages.error(request, "Please check your payment form again.")
    #     return redirect(reverse('view_payment'))


    else:
        print(payment_form.errors)
        messages.error(request, "Your payment form was not valid")
        return redirect(reverse('view_payment'))


def view_confirm(request):

    return render(request, 'confirm.html')