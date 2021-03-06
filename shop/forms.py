from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('headline', 'rating', 'review_text')
        exclude = ('user', 'item',)
