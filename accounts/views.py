from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

def view_logreg(request):
    return render(request, 'logreg.html')


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST' and id == 'registerform':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('view_cart'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        registerform = UserRegistrationForm()

    args = {'registerform': registerform}
    return render(request, 'view_cart', args)


# def logout(request):
#     """A view that logs the user out and redirects back to the index page"""
#     auth.logout(request)
#     messages.success(request, 'You have successfully logged out')
#     return redirect(reverse('view_home'))


# def login(request):
#     """A view that manages the login form"""
#     if request.method == 'POST':
#         user_form = UserLoginForm(request.POST)
#         if user_form.is_valid():
#             user = auth.authenticate(request.POST['username_or_email'],
#                                      password=request.POST['password'])

#             if user:
#                 auth.login(request, user)
#                 messages.error(request, "You have successfully logged in")

#                 if request.GET and request.GET['next'] !='':
#                     next = request.GET['next']
#                     return HttpResponseRedirect(next)
#                 else:
#                     return redirect(reverse('index'))
#             else:
#                 user_form.add_error(None, "Your username or password are incorrect")
#     else:
#         user_form = UserLoginForm()

#     args = {'user_form': user_form, 'next': request.GET.get('next', '')}
#     return render(request, 'login.html', args)


# @login_required
# def profile(request):
#     """A view that displays the profile page of a logged in user"""
#     return render(request, 'profile.html')


