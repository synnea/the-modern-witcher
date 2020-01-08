from django.shortcuts import render, get_object_or_404
from .models import Item
from django.views.generic.detail import DetailView

class ItemDetailView(DetailView):

    model = Item
    template_name = 'item_details.html'
    context_object_name = 'item'
    
    def get_item(self, id=id):
        _id = self.kwargs.get('pk')
        product = get_object_or_404(Item, id=_id)

        return render(id, 'item_details.html', {'product': product})