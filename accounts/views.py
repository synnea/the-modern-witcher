from django.shortcuts import render

def view_logreg(request):
    return render(request, 'logreg.html')
