from django.test import TestCase
from .models import Profile

class TestItemModel(TestCase):

    def test_can_create_new_profile_model_instance(self):
        """This test checks if a user who  has not previously
        saved any of their information can save their profile."""

        def setUp(self):
            self.credentials = {
                'username': 'testuser',
                'password': 'secret'}
            user = User.objects.create_user(**self.credentials)

        def test_can_create_new_profile_model_instance(self):
            profile = Profile(
                username = user.username,
                last_name = 'Smith',
                first_name = 'John',

                address1 = 'Knorrgasse 23',
                address2 = '',
                zipcode = "10247",
                country = 'Germany'
                )
            
            profile.save()
            self.assertEqual(profile.last_name, 'Smith')


    def test_can_update_existing_profile(self):        
        """This test checks if a user who  has not already
        saved their information in the profile can 
        update it."""        
                
        def setUp(self):
            self.credentials = {
                'username': 'testuser',
                'password': 'secret'}
            user = User.objects.create_user(**self.credentials)

            self.credentials = {
                'username': user.username,
                'password': 'secret',
                'last_name': 'Smith',
                'first_name': 'John',
                'address1': 'Knorrgasse 23',
                'address2': '',
                'zipcode' : "10247",
                'country' : 'Germany'
                }
            profile = Profile.objects.create(**self.credentials)

        def test_can_update_existing_profile(self):
            profile = Profile(
                username = user.username,
                last_name = 'Kerrigan',
                first_name = 'John',
                address1 = 'Knorrgasse 23',
                address2 = '',
                zipcode = "10247",
                country = 'Germany'
            )                    
            profile.save()
            self.assertEqual(profile.last_name, 'Kerrigan')