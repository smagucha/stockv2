from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.test import  TestCase
from django.contrib.auth.models import User
from django.forms.fields import Field


class FormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='newadmin', password='password1234')
        self.user.save()
        self.data = {
            'old_password': 'password123',
            'new_password1': 'password1234',
            'new_password2': 'password1234',
        }
        self.getuser = User.objects.get(pk=1)

    def test_user_creation_form(self):
        form = UserCreationForm(
            data={
                'username': 'admin',
                'password1': 'admin123',
                'password2': 'admin123'
            }
        )
        self.assertFalse(form.is_valid())

    def test_user_creation_form_no_data(self):
        form = UserCreationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_create_user_credential(self):
        required_error = [str(Field.default_error_messages['required'])]
        form = UserCreationForm(
            data={
                'username': '',
                'password1': '',
                'password2': ''
            }
        )
        self.assertEqual(form['username'].errors, required_error)
        self.assertEqual(form['password1'].errors, required_error)
        self.assertEqual(form['password2'].errors, required_error)

    def test_password_change_form(self):
        form = PasswordChangeForm(
            self.getuser,
            self.data
        )
        self.assertFalse(form.is_valid())

    def test_reset_password(self):
        form = PasswordResetForm(
            data={
                'email': 'smagucha@gmail.com'
            }
        )
        self.assertTrue(form.is_valid())

    def test_reset_password_no_data(self):
        required_error = [str(Field.default_error_messages['required'])]
        form = PasswordResetForm(
            data={
                'email': ''
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form['email'].errors, required_error)





