from goodies.models import Catergory, Product
from django.test import TestCase


class CategoryModel(TestCase):

    def setUp(self):
        Catergory.objects.create(
            name='Electronic'
        )
        Product.objects.create(
            name='samsung tv',
            productcatergory_id='1',
            weight='7 kg',
            quantity=100,
        )
        self.catname = Catergory.objects.get(id=1)
        self.product= Product.objects.get(id=1)

    def test_string_category(self):
        self.assertEqual(str(self.catname), self.catname.name)

    def test_string_product(self):
        self.assertEqual(str(self.product), self.product.name)

    def test_product(self):
        self.assertEqual(self.product.name, 'samsung tv')

    def test_category(self):
        self.assertEqual(self.catname.name, 'Electronic')
