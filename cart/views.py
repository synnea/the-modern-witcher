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
from accounts.models import User
from .models import Order, OrderLineItem
from .forms import MakePaymentForm, OrderForm
from accounts import views
import stripe
import os
import datetime

stripe.api_key = settings.STRIPE_SECRET

def view_cart(request):
    """ A view that renders the cart view."""

    if request.user.is_authenticated:

        # Save a cookie to signify that the user is on the shipping part of 
        # the checkout process. This is needed for the amend_cart function.

        shipping = True
        request.session['shipping'] = shipping

        # checks if the user already has saved their address in the account section.

        try:
            current_user = request.user
            user = Profile.objects.get(username=current_user)
            profile_form = ProfileAddressForm(instance=user)
        
        # if they haven't, instantiate an empty form.

        except:
            profile_form = ProfileAddressForm()

        if 'shipping' in request.POST:

            del request.session['shipping']

            # checks if the profile form is valid, and if it is,
            # either updates the existing data or creates a new instance.

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

        # if the user is not logged in, redirect them to logreg.
        # Save cookie that marks their access point.

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

    # if the quantity is reduced to 0, remove the item.

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(str(id))    

    request.session['cart'] = cart

    # check if the 'shipping' cookie is present.

    if request.session.get('shipping'):
        return redirect(reverse('view_cart'))

    else:    
        return redirect(reverse('view_payment'))


@login_required
def view_payment(request):
    """ View that shows the renders payment.html."""

    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    profile_form = ProfileAddressForm(instance=profile)

    payment_form = MakePaymentForm()
    order_form = OrderForm()


    context = {'profile_form': profile_form, 'payment_form': payment_form, 
            'profile': profile,
            'order_form': order_form,
            'publishable': settings.STRIPE_PUBLISHABLE}

    return render(request, 'payment.html', context)


def payment(request):
    """ View that handles all the payment functionality."""
    
    payment_form = MakePaymentForm(request.POST)
    order_form = OrderForm(request.POST)

    if payment_form.is_valid() and order_form.is_valid():

        # adds the current time zone and the logged in user to the form.

        order = order_form.save(commit=False)
        order.date = timezone.now()
        order.user = get_object_or_404(User, pk=request.user.id)
        order.save()

        cart = request.session.get('cart')
        cart_items = []
        total = 0
        product_count = 0

        # loops through all the items in the cart and inserts the
        # data into OrderLineItem objects.

        for id, quantity in cart.items():
                product = get_object_or_404(Item, pk=id)
                quantity = int(quantity)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity, 
                        user = request.user
                    )
                order_line_item.save()

        # handle Stripe functionality

        try:
            customer = stripe.Charge.create(
                amount=int(total*100),
                currency='EUR',
                description=request.user.email,
                card=payment_form.cleaned_data['stripe_id'],
                    )

        except stripe.error.CardError:
            messages.error(request, "Your card was declined!")
            
        if customer.paid:
            messages.error(request, "You have successfully paid")
            request.session['cart'] = {}
            return redirect(reverse('view_confirm'))
        else:
            messages.error(request, "Unable to take payment")
            return redirect(reverse('view_payment'))

    else:
        messages.error(request, "Your payment form was not valid")
        return redirect(reverse('view_payment'))



def view_confirm(request):
    """View that renders the confirmation page after successful payment"""

    order = Order.objects.last()

    orderline = OrderLineItem.objects.filter(order=order)

    return render(request, 'confirm.html', {'orderline': orderline})