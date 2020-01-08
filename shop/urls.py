from django.urls import path
from items.models import Item
from .views import view_all, ItemDetailView

urlpatterns = [
    path('', view_all, name="view_all"),
    path('details/<int:pk>', ItemDetailView.as_view(), name="item_details"),
]
