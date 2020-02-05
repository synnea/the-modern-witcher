from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm, ProfileAddressForm
from .models import Profile
from cart.models import Order, OrderLineItem
from cart.views import view_cart
from modern_witcher.views import home_view
from django.template.context_processors import csrf
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

def view_account(request):
    """
    Renders the account page.
    Checks if the user is logged in. If they are, fetch their
    profile from the database and instantiate it.
    Also look up their orders in the database.
    If they're not logged in, redirect to logreg page.
    """

    if request.user.is_authenticated:

        try:
            current_user = request.user
            user = Profile.objects.get(username=current_user)
            profile_form = ProfileAddressForm(instance=user)

        
        except:
            profile_form = ProfileAddressForm()

        orders = Order.objects.filter(user=request.user).order_by('-date')

        all_orders = []
        order_items = []
        print("order items were assigned")

        for order in orders:
            order_items_db = OrderLineItem.objects.filter(order=order)
            order_items = []
            order_total = 0
            for order_item in order_items_db:
                order_items.append(order_item)
                order_items = order_items
                order_total += int(order_item.product.price * order_item.quantity)
            all_orders.append({'order': order, 'order_items': order_items, "total": order_total})


        return render(request, 'myaccount.html', {'profile_form': profile_form, 'all_orders': all_orders, 'order_items': order_items})

    else:
        account = True
        request.session['account'] = account
        return redirect(reverse('logreg'))


def logreg(request):
    """ Login and registration view that renders
    the corresponding forms. """

    register_form = UserRegistrationForm()
    login_form = UserLoginForm()
    args = {'register_form': register_form, 'login_form': login_form}

    return render(request, 'logreg.html', args)


def register(request):
    """A view that manages the registration form"""

    register_form = UserRegistrationForm(request.POST)
    if register_form.is_valid():
        register_form.save()

        # if the form was valid, insert the user data into the form.

        username = register_form.cleaned_data.get('username')
        raw_password = register_form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        auth.login(request=request, user=user)
        messages.success(request, "Place of power, it's gotta be! You've been registered.")
        if request.session.get('account'):
            del request.session['account']
            return redirect(reverse('view_account'))

        elif request.session.get('cart_access'):
            del request.session['cart_access']
            return redirect(reverse('view_cart'))

            # if the form was not valid, reject the form and reload the page.
    else:
        messages.error(request, "We could not register you! Sure you re-entered your password correctly and haven't already registered?")
        return redirect(reverse('view_account'))
        

def logout(request):
    """A view that logs the user out and redirects back to the home page"""
        
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('home_view'))


def login(request):
    """A view that manages the login form"""

    login_form = UserLoginForm(request.POST)
    if login_form.is_valid():
        user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
        if user:
            auth.login(request=request, user=user)
            current_user = request.user

            # Checks if the user previously tried to access account and redirects to account

            if request.session.get('account'):
                del request.session['account']
                return redirect(reverse('view_account'))

            # Checks if the user previously tried to access the cart and redirects to cart

            elif request.session.get('cart_access'):
                del request.session['cart_access']
                return redirect(reverse('view_cart'))

        else:
            messages.error(request, "Wind's howling... your credentials are incorrect.")
            return redirect(reverse('logreg'))

    else:
        messages.error(request, "Wind's howling... something went wrong.")
        return redirect(reverse('view_account'))



@login_required
def save_address(request):
    """ A view that saves the address in the Profile model.
    It updates the profile model if no address had been saved before.
    Otherwise, it creates a new profile instance. """
     
    form = ProfileAddressForm(request.POST)
    if form.is_valid():
        user = request.user
        profile = form.cleaned_data
        obj, created = Profile.objects.update_or_create(username=user, defaults=profile)
        if created:
            messages.success(request, 'Thanks for saving your address!')
        else:
            messages.success(request, 'Updated successfully.')

        profile_form = ProfileAddressForm(request.POST)        
        return render(request, 'myaccount.html', {'profile_form': profile_form} )
    
    else:
        messages.error(request, 'Sharpen your eyes, Witcher! Something went wrong.')
        return redirect(reverse('view_account'))




