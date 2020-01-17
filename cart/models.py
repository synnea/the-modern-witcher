from django.db import models
from django.contrib.auth.models import User
from items.models import Item
import datetime


class Order(models.Model):

    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    products = models.ManyToManyField(Item)
    quantity = models.IntegerField(blank=False, default=0)
    date = models.DateField(default=datetime.date.today, null=True)
    
    def __str__(self):
        return "{0} @ {1} {2}".format(self.user, self.products, self.quantity)


# len(carina.orders.products.filter(pk=item_to_review.pk)) == 0
# view level
