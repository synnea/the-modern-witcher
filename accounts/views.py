from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm, ProfileAddressForm
from .models import Profile
from cart.views import view_cart
from modern_witcher.views import home_view
from django.template.context_processors import csrf
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

def view_account(request):

    if request.user.is_authenticated:

        try:
            current_user = request.user
            user = Profile.objects.get(username=current_user)
            profile_form = ProfileAddressForm(instance=user)
            return render(request, 'myaccount.html', {'profile_form': profile_form})
        
        except:
            profile_form = ProfileAddressForm()
            return render(request, 'myaccount.html', {'profile_form': profile_form})

    else:

        register_form = UserRegistrationForm()
        login_form = UserLoginForm()
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
            current_user = request.user
            user = Profile.objects.get(username=current_user)
            profile_form = ProfileAddressForm(instance=user)

            if request.session.get('account'):
                return render(request, 'myaccount.html', {'profile_form': profile_form})

            else:
                return redirect(reverse('view_cart'))

        else:
            messages.error(request, "Wind's howling... your credentials are incorrect.")
            return redirect(reverse('view_account'))

    else:
        messages.error(request, "Wind's howling... something went wrong.")
        return redirect(reverse('view_account'))



@login_required
def save_address(request):
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




