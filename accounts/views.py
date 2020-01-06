from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm
from modern_witcher.views import home_view
from django.template.context_processors import csrf
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def view_account(request):

    if request.user.is_authenticated:
        return render(request, 'myaccount.html')

    else:

        register_form = UserRegistrationForm(request.POST)
        login_form = UserLoginForm(request.POST)
        account = True
        request.session['account'] = account
        args = {'register_form': register_form, 'login_form': login_form}

        return render(request, 'logreg.html', args)



def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('view_cart'))

            else:
                messages.error(request, "unable to log you in at this time!")

        else:
            messages.error(request, "form was not valid")
            return redirect(reverse("view_account") )
    else:
        register_form = UserRegistrationForm()

    args = {'register_form': register_form}
    return render(request, 'cart.html', args)


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
        return render(request, 'myaccount.html')

    else:
        return render(request, 'cart.html')


