from django.urls import path
from .views import view_logreg

urlpatterns = [
    path('', view_logreg, name="view_logreg")
]