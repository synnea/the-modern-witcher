from items.models import Item
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic.detail import DetailView

class ItemDetailView(DetailView):

    model = Item
    template_name = 'item_details.html'
    context_object_name = 'product'
    extra_context = {}
    
    def get_object(self, queryset=Item):
        _id = int(self.kwargs.get('pk'))
        print(_id)
        instance = get_object_or_404(Item, id=_id)
        self.extra_context['product'] = instance
        print(instance)
        return instance

# def get_detail(request, kwargs):
#     product = get_object_or_404(Item, pk=kwargs)
#     return render(request, 'item_details.html', {'product': product})