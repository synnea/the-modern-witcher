from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from items.models import Item
import datetime


class Order(models.Model):

    objects = models.Manager()

    full_name = models.CharField(max_length=50, blank=False, default="Test")
    phone_number = models.CharField(max_length=20, blank=False, default=0)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today, null=True)
    
    def __str__(self):
        return "{0} @ {1}".format(self.full_name, self.date)



class OrderLineItem(models.Model):

    objects = models.Manager()
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1}".format(
            self.quantity, self.product.name)


# len(carina.orders.products.filter(pk=item_to_review.pk)) == 0
# view level