from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm, UserAddressForm
from modern_witcher.views import home_view
from django.template.context_processors import csrf
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def view_account(request):

    if request.user.is_authenticated:
        user = request.user
        address_form = UserAddressForm(request.POST)

        return render(request, 'myaccount.html', {'user': user, 'address_form': address_form})

    else:

        register_form = UserRegistrationForm(request.POST)
        login_form = UserLoginForm(request.POST)
        account = True
        request.session['account'] = account
        args = {'register_form': register_form, 'login_form': login_form}

        return render(request, 'logreg.html', args)



def register(request):
    """A view that manages the registration form"""

    register_form = UserRegistrationForm(request.POST)
    if register_form.is_valid():
        register_form.save()

        username = register_form.cleaned_data.get('username')
        raw_password = register_form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        auth.login(request=request, user=user)
        messages.success(request, "Place of power, it's gotta be! You've been registered.")
        if request.session.get('account'):
            return redirect(reverse('view_account'))

        else:
            return render(request, 'cart.html')
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
            messages.success(request, "Welcome back, witcher!")

        else:
            messages.error(request, "Wind's howling... your credentials are incorrect.")
            return redirect(reverse('view_account'))

    else:
        return redirect(reverse('view_account'))

    if request.session.get('account'):
        address_form = UserAddressForm()
        return render(request, 'myaccount.html', {'address_form':address_form})

    else:
        return render(request, 'cart.html')


def save_address(request):

    address_form = UserAddressForm(request.POST)
    if address_form.is_valid():
        address_form.save()
        return redirect(reverse(view_account))

    else:
        messages.error(request, "Sharpen your eyes, Witcher! Something went wrong.")


