from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

def view_logreg(request):

    user_form = UserRegistrationForm(request.POST)
    args = {'user_form': user_form}

    return render(request, 'logreg.html', args)



def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        print("request activated")
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            print("userformisvalid")
            user_form.save()

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
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'cart.html', args)

    


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


