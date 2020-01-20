from items.models import Item
from cart.models import OrderLineItem, Order
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic.detail import DetailView

class ItemDetailView(DetailView):

    model = Item
    template_name = 'item_details.html'
    context_object_name = 'product'

    def get_context_data(self, queryset=Item, **kwargs):

        _id = int(self.kwargs.get('pk'))
        item = get_object_or_404(Item, id=_id)

        user = self.request.user

        try:
            ordered_items = OrderLineItem.objects.filter(user=user, product=item)[0]
            purchased = "Yes, bought"

        except:
            purchased = "No, not bought"

        product = {'item': item, 'purchased': purchased}

        return product





