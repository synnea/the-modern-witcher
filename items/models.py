from django.db import models
from django.urls import reverse

class Item(models.Model):

    
    objects = models.Manager()

    ARMORER = 'Armor'
    BLACKSMITH = 'Weapons'
    HERBALIST = 'Ingredients'
    OTHER = 'Other'

    CATEGORY_CHOICES = [
        (ARMORER, 'Armor'),
        (BLACKSMITH, 'Weapons'),
        (HERBALIST, 'Ingredients'),
        (OTHER, 'Other')
    ]

    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=OTHER,
    )


    height = models.DecimalField(max_digits=3, decimal_places=1)
    width = models.DecimalField(max_digits=3, decimal_places=1)
    weight = models.DecimalField(max_digits=3, decimal_places=1)

    origin = models.CharField(max_length=100, blank=True)

    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='item_images')

    featured = models.BooleanField(default=False)

    def get_item_details(self):
        """ Gets absolute url including listing id as pk for dynamic url """
        id = int(self.pk)
        return reverse('item_details', kwargs={'pk': id})

    def __str__(self):
        return self.name