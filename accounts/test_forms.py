from django.test import TestCase
from accounts.forms import UserLoginForm, UserRegistrationForm

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
