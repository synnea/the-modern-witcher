from django.urls import path
from .views import ItemDetailView

urlpatterns = [
    path('details/<int:pk>', ItemDetailView.as_view(), name="item_details"),
]
