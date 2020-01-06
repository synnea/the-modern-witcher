from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=30, blank=False)
    first_name = models.CharField(max_length=30, blank=False)
    address1 = models.CharField(max_length=30, blank=False)
    address2 = models.CharField(max_length=30, blank=True)
    zipcode = models.CharField(max_length=20, blank=False)
    country = CountryField()

    @receiver(post_save, sender=User)
    def save_user_profile(self, sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user
