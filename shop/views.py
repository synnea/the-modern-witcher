from django.shortcuts import render, redirect, reverse
from items.models import Item
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.contrib import messages


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
        review_form.save(commit=False)

        review_form.user = request.user
        review_form.reviewed_item = id

        review_form.save()
        
        messages.success(request, "Thank you for telling us what you think!")
        return redirect('product.get_item_details')


    else: 
        messages.error(request, "Sorry, we could not save your review.")
        return redirect(reverse('product.get_item_details'))