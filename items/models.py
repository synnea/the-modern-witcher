from django.db import models

class Item(models.Model):

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

    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='item_images')

    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name