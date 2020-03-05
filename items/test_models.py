from django.test import TestCase
from .models import Item
from django.contrib.auth.models import User
import datetime


class TestOrderModel(TestCase):

    def test_can_create_new_item_model_instance(self):
        item = Item(
                name='Test Product',
                description='Test description',
                category='BLACKSMITH',
                height='4',
                weight='4',
                width='4',
                price='50'
                )

        item.save()
        self.assertEqual(item.name, 'Test Product')
