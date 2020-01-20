from items.models import Item
from cart.models import OrderLineItem, Order
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic.detail import DetailView
from shop.forms import ReviewForm
from shop.models import Review

class ItemDetailView(DetailView):
    """ A detailed view for the shop items."""

    model = Item
    template_name = 'item_details.html'
    context_object_name = 'product'

    def get_context_data(self, queryset=Item, **kwargs):
        """ Function that createst the context to be renders on the detail page.
        Fetches the item by id, and determines if the user has already bought
        that very item by checking against the database.
        Then it checks if reviews have been submitted for the item, and 
        collects them in a separate object. """

        _id = int(self.kwargs.get('pk'))
        item = get_object_or_404(Item, id=_id)

        user = self.request.user

        try:
            ordered_items = OrderLineItem.objects.filter(user=user, product=item)[0]
            purchased = True

        except:
            purchased = False

        try:
            reviews = Review.objects.filter(reviewed_item=item)

        except:
            reviews = False

        review_form = ReviewForm()

        product = {'item': item, 'purchased': purchased, 
        'review_form': review_form, 'reviews': reviews}

        return product




