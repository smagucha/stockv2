from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class Account_Tests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='newadmin', password='password1234')
        self.user.save()
        self.data = {
            'old_password': 'password123',
            'new_password1': 'password1234',
            'new_password2': 'password1234',
        }
        self.getuser = User.objects.get(pk=1)

    def test_create_user(self):
        response = self.client.post(
            reverse('signup'),
            {
                'username': 'admin',
                'password': 'admin123',
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_login_post(self):
        response = self.client.post(
            reverse('login'),
            data={'username': 'admin', 'password': 'admin123'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_change_password_post(self):
        response = self.client.post(
            reverse('password_change'),
            self.data
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/accounts/login/?next=/accounts/password_change/')

    def test_reset_password_post(self):
        response = self.client.post(
            reverse('password_reset'),
            data={
               ' email': 'smagucha@gmail.com'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/accounts/reset_password_sent/')
