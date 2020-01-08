from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Item
from django.views.generic.detail import DetailView

class ItemDetailView(DetailView):

    model = Item
    template_name = 'item_details.html'
    
    def get_object(self, queryset=Item):
        _id = int(self.kwargs.get('pk'))
        print(_id)
        product = get_object_or_404(Item, pk=_id)
        print(product)
        return product

def get_detail(request, kwargs):
    product = get_object_or_404(Item, pk=kwargs)
    return render(request, 'item_details.html', {'product': product})