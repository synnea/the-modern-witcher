from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=30, required=True)
    first_name = models.CharField(max_length=30, required=True)
    address1 = models.CharField(max_length=30, required=True)
    address2 = models.CharField(max_length=30, required=False)
    zipcode = models.CharField(max_length=20, required=True)
    country = CountryField()

    @receiver(post_save, sender=User)
    def save_user_profile(self, sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user
