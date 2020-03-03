from django.test import TestCase
from accounts.forms import UserLoginForm, UserRegistrationForm, ProfileAddressForm
from django.contrib.auth.models import User

# Create your tests here.

class TestAccountForms(TestCase):
    def test_can_create_a_user(self):
        form = UserRegistrationForm({'username': 'tester1',
                                     'email': 'tester1@email.com',
                                     'password1': 'testing321',
                                     'password2': 'testing321'})
        self.assertTrue(form.is_valid())

    def test_validation_error_is_raised(self):
        form = UserRegistrationForm({'username': 'tester1',
                                     'email': 'tester1@email.com',
                                     'password1': 'testing321',
                                     'password2': 'wrongpassword'})
        self.assertFalse(form.is_valid())

    def test_can_login(self):
        form = UserLoginForm({'username': 'tester',
            'password': 'test123456'})
        self.assertTrue(form.is_valid())

    def test_user_can_add_profile_form_in_account_settings(self):
        def setUp(self):
            self.credentials = {
                'username': 'testuser',
                'password': 'secret'}
            User.objects.create_user(**self.credentials)

        def test_user_can_add_profile_form_in_account_settings(self):
            form = ProfileAddressForm({'username': 'testuser',
                                        'last_name': 'Smith',
                                        'first_name': 'John',
                                        'address1': 'Knorrgasse 23',
                                        'address2': '',
                                        'zipcode': "10247",
                                        'country': 'Germany'
            })
            self.assertTrue(form.is_valid())



