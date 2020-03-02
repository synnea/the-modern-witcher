from django.test import TestCase
from .models import Review
from shop.models import Item
from cart.models import Order, OrderLineItem
from django.contrib.auth.models import User
import datetime       
        

        
class TestReviewModel(TestCase):

    def test_can_create_new_review_model_instance(self):
        """This test checks if a new order model instance can
        be created."""        
                
        def setUp(self):
            self.credentials = {
                'username': 'testuser',
                'password': 'secret'}
            user = User.objects.create_user(**self.credentials)

            def test_can_create_new_review(self):
                order = Order(
                    username = user.username,
                    full_name = 'Jon Snow',
                    date = datetime.date.today,
                    phone_number = "004915145113456"
                    )
            
                order.save()

            
                self.assertEqual(order.full_name, 'Jon Snow')