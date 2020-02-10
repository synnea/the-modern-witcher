from django.test import TestCase
from django.contrib.auth.models import User

class TestViews(TestCase):
    def test_get_logreg_screen(self):
        page = self.client.get("/user/logreg/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'logreg.html')


    def test_login(self):
        def setUp(self):
            self.credentials = {
                'username': 'testuser',
                'password': 'secret'}
            User.objects.create_user(**self.credentials)
        
        def test_login(self):
            # send login data
            response = self.client.post('/user/myaccount/', self.credentials, follow=True)
            # should be logged in now
            self.assertTrue(response.context['user'].is_authenticated)


    def test_register_new_user(self):

        page = self.client.get('/user/register/')
        created = User.objects.create_user(
            username='tester', email='tester@user.com', password="badasstesting"
        )
        self.assertTrue(page.status_code, 200)
        self.assertTrue(created)
