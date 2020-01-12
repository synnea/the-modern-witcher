from django.shortcuts import render, redirect, reverse
from items.models import Item

def view_all(request):
    products = Item.objects.all()

    categories = dict(Item.CATEGORY_CHOICES)
    categories = categories.values()

    return render(request, 'shop.html', {'products': products, 'categories': categories})


def view_categories(request, category):

    print(category)

    categories = dict(Item.CATEGORY_CHOICES)
    categories = categories.values()
    
    products = Item.objects.filter(category=category)
    return render(request, 'shop.html', {'products': products, 'categories': categories})
