from django.shortcuts import render, redirect, reverse
from items.models import Item
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


def view_all(request):
    products = Item.objects.all()

    categories = dict(Item.CATEGORY_CHOICES)
    categories = categories.values()

    return render(request, 'shop.html', {'products': products, 'categories': categories})


def view_categories(request, category):

    categories = dict(Item.CATEGORY_CHOICES)
    categories = categories.values()
    
    products = Item.objects.filter(category=category)
    return render(request, 'shop.html', {'products': products, 'categories': categories})


@login_required
def submit_review(request, id):

    review_form = ReviewForm(request.POST)

    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = get_object_or_404(User, pk=request.user.id)
        review.reviewed_item = get_object_or_404(Item, pk=id)
        

        review_form.save()
        product = Item.objects.get(pk=id)
        messages.success(request, "Thank you for telling us what you think!")
        return redirect('view_all')


    else: 
        product = Item.objects.get(pk=id)
        messages.error(request, "Sorry, we could not save your review.")
        return redirect(reverse('view_all'))