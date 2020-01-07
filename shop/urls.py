from django.urls import path
from .views import view_all

urlpatterns = [
    path('', view_all, name="view_all")
]
