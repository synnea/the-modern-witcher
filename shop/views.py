from django.shortcuts import render, get_object_or_404
from items.models import Item
from django.views.generic.detail import DetailView

def view_all(request):
    products = Item.objects.all()

    return render(request, 'shop.html', {'products': products})

