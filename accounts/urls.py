from django.urls import path
from .views import view_logreg, register, login

urlpatterns = [
    path('', view_logreg, name="view_logreg"),
    path('register/', register, name="register"),
    path('login/', login, name="login")
]