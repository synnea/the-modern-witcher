from django.shortcuts import render
from items.models import Item

def home_view(request):
    """ A view that renders the home page. 
    Looks up items that are featured. """

    featured = Item.objects.filter(featured="True")[:3]
    
    return render(request, 'index.html', {'featured': featured})