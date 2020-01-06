from django.urls import path
from .views import view_account, register, login, logout, save_address

urlpatterns = [
    path('', view_account, name="view_account"),
    path('register/', register, name="register"),
    path('myaccount/', login, name="login"),
    path('logout/', logout, name='logout'),
    path('saveaddress', save_address, name="save_address")
]