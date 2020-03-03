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
                item = Item(
                        name = 'Test Product',
                        description = 'Test description',
                        category = 'BLACKSMITH',
                        height = '4',
                        weight = '4',
                        width = '4',
                        price = '50'
                        )
                    
                item.save()

                review = Review(
                    user = user.username,
                    reviewed_item = item.name,
                    headline = "An exciting new product",
                    rating = '5',
                    review_text = "test test test test test"
                )

                review.save()
                self.assertEqual(review.headline, 'An exciting new product')
            