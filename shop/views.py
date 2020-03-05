from django.shortcuts import render, redirect, reverse
from items.models import Item
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


def view_all(request):
    """ Fetches all  items available in the databse.
    and renders them to shop html. """
    products = Item.objects.all()

    categories = dict(Item.CATEGORY_CHOICES)
    categories = categories.values()

    return render(request, 'shop.html', {'products': products, 'categories': categories})


def view_categories(request, category):
    """ Fetches all items belonging to a certain category. """

    categories = dict(Item.CATEGORY_CHOICES)
    categories = categories.values()

    products = Item.objects.filter(category=category)
    return render(request, 'shop.html', {'products': products, 'categories': categories})


@login_required
def submit_review(request, id):
    """A view that lets users submit reviews of items
    that they have already purchased. """

    item = get_object_or_404(Item, id=id)

    review_form = ReviewForm(request.POST)
    user = request.user

    if review_form.is_valid():

        # Check if the user actually purchased the item they're
        # trying to review in order to prevent review fraud.

        try:
            ordered_items = OrderLineItem.objects.filter(user=user, product=item)[0]

            review = review_form.save(commit=False)
            review.user = get_object_or_404(User, pk=request.user.id)
            review.reviewed_item = get_object_or_404(Item, pk=id)

            review_form.save()
            messages.success(request, "Thank you for telling us what you think!")
            return redirect('view_all')

        except:
                messages.error(request, "Sorry, you are not authorized to review this item")

    else:
        messages.error(request, "Something went wrong in your review form.")
        return redirect(reverse('view_all'))
