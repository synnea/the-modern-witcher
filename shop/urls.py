from django.urls import path
from items.models import Item
from .views import view_all

urlpatterns = [
    path('', view_all, name="view_all")
]
