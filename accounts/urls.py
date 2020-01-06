from django.urls import path
from .views import view_account, register, login, logout

urlpatterns = [
    path('', view_account, name="view_account"),
    path('register/', register, name="register"),
    path('myaccount/', login, name="login"),
    path('logout/', logout, name='logout')
]