from django.contrib.auth.views import LoginView, PasswordResetView
from django.test import TestCase
from django.urls import resolve, reverse
from accounts.views import SignUpView


class UrlTest(TestCase):
    def test_sign_up_url(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_sign_up_view_name(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func.view_class, SignUpView)

    def test_login_url(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_name(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, LoginView)

    def test_change_password(self):
        response = self.client.get(
            reverse('password_change'),
        )
        self.assertEqual(response.status_code, 302)

    def test_reset_password_url(self):
        response = self.client.get(reverse('password_reset'))
        url = reverse('password_reset')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resolve(url).func.view_class, PasswordResetView)
