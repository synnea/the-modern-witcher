from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm

# Create your tests here.

class TestAccountForm(TestCase):

    def test_can_login(self):

        form = UserLoginForm({'username': 'carina', 'password': ''})

