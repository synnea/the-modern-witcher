
from django.db import models
from django.contrib.auth.models import User
from items.models import Item

class Review(models.Model):

    RATING_CHOICES = (
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewed_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    headline = models.CharField(max_length=25, blank=False)
    rating = models.CharField(max_length=1,choices=RATING_CHOICES, blank=False)
    review_text = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return "{0} reviewed {1}".format(self.user, self.reviewed_item)

# user can only review item that they thought



