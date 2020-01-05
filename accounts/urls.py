from django.urls import path
from .views import view_logreg, register, login, logout

urlpatterns = [
    path('', view_logreg, name="view_logreg"),
    path('register/', register, name="register"),
    path('myaccount/', login, name="login"),
    path('logout/', logout, name='logout')
]