from items.models import Item
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic.detail import DetailView

class ItemDetailView(DetailView):

    model = Item
    template_name = 'item_details.html'
    context_object_name = 'product'
    
    def get_object(self, queryset=Item):
        _id = int(self.kwargs.get('pk'))
        product = get_object_or_404(Item, id=_id)

        return product