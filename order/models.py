from django.db import models
from django.contrib.auth.models import User
from items.models import Item

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} @ {1} {2}".format(self.user, self.product.name, self.quantity)