from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    username = models.ForeignKey(User,on_delete=models.CASCADE, default=None)
    last_name = models.CharField(max_length=30, blank=False)
    first_name = models.CharField(max_length=30, blank=False)
    address1 = models.CharField(max_length=30, blank=False)
    address2 = models.CharField(max_length=30, blank=True)
    zipcode = models.CharField(max_length=20, blank=False)
    country = CountryField()

    def __str__(self):
        return self.last_name
