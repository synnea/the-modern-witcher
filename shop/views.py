from django.shortcuts import render
from items.models import Item

def view_all(request):
    products = Item.objects.all()

    return render(request, 'shop.html', {'products': products})

