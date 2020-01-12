from django.urls import path
from items.models import Item
from .views import view_all, view_categories

urlpatterns = [
    path('', view_all, name="view_all"),
    path('category/<str:category>', view_categories, name="view_categories"),
]
