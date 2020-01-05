from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def view_logreg(request):

    register_form = UserRegistrationForm(request.POST)
    login_form = UserLoginForm(request.POST)
    args = {'register_form': register_form, 'login_form': login_form}

    return render(request, 'logreg.html', args)



def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        print("request activated")
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            print("userformisvalid")
            register_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                print("userisvalid")
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('view_cart'))

            else:
                print("was not valid")
                messages.error(request, "unable to log you in at this time!")

        else:
            messages.error(request, "form was not valid")
            return redirect(reverse("view_logreg") )
    else:
        register_form = UserRegistrationForm()

    args = {'register_form': register_form}
    return render(request, 'cart.html', args)

    


def logout(request):
    print("logout activated")
    """A view that logs the user out and redirects back to the index page"""
    if request.method == 'POST':
        print("logout activated")         
        auth.logout(request)
        messages.success(request, 'You have successfully logged out')
        return redirect(reverse('view_home'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            print("user login form is valid")
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('view_logreg'))
            else:
                messages.error(request, "Your username or password are incorrect")
                login_form.add_error(None, "Your username or password are incorrect")
                return redirect(reverse('view_logreg'))

        else:
            messages.error(request, "We could not log you in")
            return redirect(reverse('view_logreg'))

    args = {'login_form': login_form, 'next': request.GET.get('next', '')}
    return render(request, 'myaccount.html', args)


# @login_required
# def profile(request):
#     """A view that displays the profile page of a logged in user"""
#     return render(request, 'profile.html')


