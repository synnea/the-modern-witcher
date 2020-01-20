from items.models import Item
from cart.models import OrderLineItem, Order
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic.detail import DetailView
from shop.forms import ReviewForm

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
            purchased = True

        except:
            purchased = False

        review_form = ReviewForm()

        product = {'item': item, 'purchased': purchased, 'review_form': review_form}

        return product





