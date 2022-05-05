from django.test import TestCase
from sale.models import Sale, Order
from goodies.models import Product, Catergory
from django.contrib.auth.models import User


class SaleModelTest(TestCase):

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

    def test_str_sale(self):
        self.assertEqual(str(self.sale), self.sale.serverby.username)

    def test_str_order(self):
        self.assertEqual(str(self.order), self.order.buyer)

    def test_sale(self):
        self.assertEqual(self.sale.serverby.username, 'admin')

    def test_order(self):
        self.assertEqual(self.order.buyer, 'cythnia')

