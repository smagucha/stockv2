from django.test import TestCase
from django.urls import reverse
from django import forms

from sale.models import Sale
from django.contrib.auth.models import User
from goodies.models import Catergory, Product

from sale.models import Order


class SaleTestUrl(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='admin', password=123456)
        self.client.login(username='admin', password=123456)
        self.category = Catergory.objects.create(
            name='Electronic'
        )
        self.product = Product.objects.create(
            name='samsung tv',
            productcatergory=self.category,
            weight='7 kg',
            quantity=100,
        )
        self.sale = Sale.objects.create(
            serverby=self.user,
            buyer='cynthia',
            buyercontact='13215',
            clientemail='cyntia@gmal.com',
            item=self.product,
            quantity=7,
        )
        self.saleid = Sale.objects.get(pk=1)
        self.data = {
            'serverby': self.user,
            'buyer': 'cynthia',
            'buyercontact': '13215',
            'clientemail': 'cyntia@gmal.com',
            'item': self.product,
            'quantity': 7,
        }

    def test_sale_list(self):
        response = self.client.get(reverse('SaleList'))
        self.assertEqual(response.status_code, 302)

    def test_sale_create(self):
        response = self.client.post(
            reverse('SaleCreate'),
            self.data
        )
        self.assertEqual(response.status_code, 302)

    def test_sale_update(self):
        response = self.client.post(
            reverse('SaleUpdate', kwargs={
                'pk': self.saleid.pk
            }),
            self.data
        )
        self.assertEqual(response.status_code, 302)

    def test_sale_delete(self):
        response = self.client.post(
            reverse('DeleteSale', kwargs={
                'pk': self.saleid.pk
            }),
            self.data
        )
        self.assertEqual(response.status_code, 302)


class OrderTestUrl(TestCase):

    def setUp(self):
        self.category = Catergory.objects.create(
            name='Electronic'
        )
        self.productname = Product.objects.create(
            name='samsung tv',
            productcatergory=self.category,
            weight='7 kg',
            quantity=100,
        )
        Order.objects.create(
            buyer='cythnia',
            email='a@a.ckd',
            phonenumber=54565,
            product=self.productname,
            quantity=7,
        )
        self.data = {
            'buyer': 'cythnia',
            'email': 'a@a.ckd',
            'phonenumber': 54565,
            'product': self.productname,
            'quantity': 7,
        }
        self.order = Order.objects.get(pk=1)

    def test_order_list(self):
        response = self.client.get(reverse('OrderList'))
        self.assertEqual(response.status_code, 302)

    def test_order_create(self):
        response = self.client.post(
            reverse('OrderCreate'),
            self.data
        )
        self.assertEqual(response.status_code, 302)

    def test_post(self):
        response = self.client.get(reverse('OrderList'))
        self.productname.quantity -= self.data['quantity']
        self.assertEqual(response.status_code, 302)

    def test_order_delete(self):
        response = self.client.delete(
            reverse('OrderDelete', kwargs={
                'pk': self.order.pk
            }),
            self.data
        )
        self.assertEqual(response.status_code, 302)

    def test_post(self):
        form = forms
