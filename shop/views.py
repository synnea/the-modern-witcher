from django.shortcuts import render
from items.models import Item

def view_all(request):
    products = Item.objects.all()

    categories = dict(Item.CATEGORY_CHOICES)
    categories = categories.values()
    print(categories)

    return render(request, 'shop.html', {'products': products, 'categories': categories})

