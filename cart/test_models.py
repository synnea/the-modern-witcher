from django.test import TestCase
from .models import Order, OrderLineItem
from shop.models import Item
from django.contrib.auth.models import User
import datetime


class TestOrderModel(TestCase):

    def test_can_create_new_order_model_instance(self):
        """This test checks if a new order model instance can
        be created."""

        def setUp(self):
            self.credentials = {
                'username': 'testuser',
                'password': 'secret'}
            user = User.objects.create_user(**self.credentials)

            def test_can_create_new_order_model_instance(self):
                order = Order(
                    username=user.username,
                    full_name='Jon Snow',
                    date=datetime.date.today,
                    phone_number="004915145113456"
                    )

                order.save()
                self.assertEqual(order.full_name, 'Jon Snow')

    def test_can_create_new_orderlineitem_model_instance(self):
        """This test checks if a new order model instance can
        be created."""

        def setUp(self):
            self.credentials = {
                'username': 'testuser',
                'password': 'secret'}
            user = User.objects.create_user(**self.credentials)

            self.credentials = {
                'username': user.username,
                'full_name': 'Jon Snow',
                'date': datetime.date.today,
                'phone_number': "004915145113456"}
            order = Order.objects.create(**self.credentials)

            def test_can_create_new_order_model_instance(self):
                orderitem = OrderLineItem(
                    product=Item.objects.filter(pk=1),
                    quantity='2',
                    date=datetime.date.today,
                    phone_number="004915145113456"
                    )

                orderitem.save()
                self.assertEqual(orderitem.quantity, '2')
