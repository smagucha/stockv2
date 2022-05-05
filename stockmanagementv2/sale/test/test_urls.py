from django.test import TestCase
from django.urls import reverse, resolve
from sale.models import Sale, Order
from goodies.models import Product, Catergory
from sale.views import SaleCreate, SaleList, SaleUpdate, DeleteSale, OrderList, OrderCreate, OrderDelete
from django.contrib.auth.models import User


class Sale_Order_Url(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='admin', password=123456)
        self.category = Catergory.objects.create(
            name='Electronic'
        )

        self.product = Product.objects.create(
            name='samsung tv',
            productcatergory=self.category,
            weight='7 kg',
            quantity=100,
        )

        Sale.objects.create(
            serverby=self.user,
            buyer='cynthia',
            buyercontact='13215',
            clientemail='cyntia@gmal.com',
            item=self.product,
            quantity=7,
        )

        Order.objects.create(
            buyer='cythnia',
            email='a@a.ckd',
            phonenumber=54565,
            product=self.product,
            quantity=7,
        )
        self.order = Order.objects.get(pk=1)
        self.sale = Sale.objects.get(pk=1)

    def test_sale_list(self):
        url = reverse('SaleList')
        self.assertEqual(resolve(url).func.view_class, SaleList)

    def test_sale_create(self):
        url = reverse('SaleCreate')
        self.assertEqual(resolve(url).func.view_class, SaleCreate)

    def test_sale_update(self):
        url = reverse('SaleUpdate', kwargs={'pk': self.sale.pk})
        self.assertEqual(resolve(url).func.view_class, SaleUpdate)

    def test_delete_sale(self):
        url = reverse('DeleteSale', kwargs={'pk': self.sale.pk})
        self.assertEqual(resolve(url).func.view_class, DeleteSale)

    def test_order_list(self):
        url = reverse('OrderList')
        self.assertEqual(resolve(url).func.view_class, OrderList)

    def test_order_create(self):
        url = reverse('OrderCreate')
        self.assertEqual(resolve(url).func.view_class, OrderCreate)

    def test_order_delete(self):
        url = reverse('OrderDelete', kwargs={'pk': self.order.pk})
        self.assertEqual(resolve(url).func.view_class, OrderDelete)

    def test_not_logged_in_sale_list(self):
        response = self.client.get(reverse('SaleList'))
        self.assertRedirects(response, '/accounts/login/?next=/sale/')

    def test_not_logged_in_sale_create(self):
        response = self.client.get(reverse('SaleCreate'))
        self.assertRedirects(response, '/accounts/login/?next=/sale/SaleCreate/')

    def test_not_logged_in_sale_update(self):
        response = self.client.get(reverse('SaleUpdate', kwargs={'pk': self.sale.pk}))
        self.assertRedirects(response, '/accounts/login/?next=/sale/SaleUpdate/1/')

    def test_not_logged_in_sale_delete(self):
        response = self.client.get(reverse('DeleteSale', kwargs={'pk': self.sale.pk}))
        self.assertRedirects(response, '/accounts/login/?next=/sale/DeleteSale/1/')

    def test_order_list(self):
        response = self.client.get(reverse('OrderList'))
        self.assertRedirects(response, '/accounts/login/?next=/sale/OrderList')

    def test_order_create(self):
        response = self.client.get(reverse('OrderCreate'))
        self.assertRedirects(response, '/accounts/login/?next=/sale/OrderCreate/')

    def test_order_delete(self):
        response = self.client.get(reverse('OrderDelete', kwargs={'pk': self.order.pk}))
        self.assertRedirects(response, '/accounts/login/?next=/sale/OrderDelete/1/')
