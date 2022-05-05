from django.test import TestCase
from django.urls import reverse, resolve
from goodies.views import (
    ProductList,
    ProductCreate,
    ProductUpdate,
    DeleteProduct,
    CategoryList,
    CategoryCreate,
    CategoryUpdate,
    DeleteCategory,
)
from goodies.models import Product, Catergory


class TestURLsTestCase(TestCase):
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
        self.product = Product.objects.get(pk=1)
        self.category = Catergory.objects.get(pk=1)

    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, ProductList)

    def test_product_create_url(self):
        url = reverse('ProductCreate')
        self.assertEqual(resolve(url).func.view_class, ProductCreate)

    def test_product_update_url(self):
        url = reverse('ProductUpdate', kwargs={'pk': self.product.pk})
        self.assertEqual(resolve(url).func.view_class, ProductUpdate)

    def test_product_delete_url(self):
        url = reverse('DeleteProduct', kwargs={'pk': self.product.pk})
        self.assertEqual(resolve(url).func.view_class, DeleteProduct)

    def test_category_list_url(self):
        url = reverse('CategoryList')
        self.assertEqual(resolve(url).func.view_class, CategoryList)

    def test_category_create_url(self):
        url = reverse('CategoryCreate')
        self.assertEqual(resolve(url).func.view_class, CategoryCreate)

    def test_category_update_url(self):
        url = reverse('CategoryUpdate', kwargs={'pk': self.category.pk})
        self.assertEqual(resolve(url).func.view_class, CategoryUpdate)

    def test_category_delete_url(self):
        url = reverse('DeleteCategory', kwargs={'pk': self.category.pk})
        self.assertEqual(resolve(url).func.view_class, DeleteCategory)

    def test_redirect_if_not_logged_in_home(self):
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, '/accounts/login/?next=/')

    def test_redirect_if_not_logged_in_product_create(self):
        response = self.client.get(reverse('ProductCreate'))
        self.assertRedirects(response, '/accounts/login/?next=/ProductCreate/')

    def test_redirect_if_not_logged_in_product_update(self):
        response = self.client.get(reverse('ProductUpdate', kwargs={'pk': self.product.pk}))
        self.assertRedirects(response, '/accounts/login/?next=/ProductUpdate/1/')

    def test_redirect_if_not_logged_in_delete_product(self):
        response = self.client.get(reverse('DeleteProduct', kwargs={'pk': self.product.pk}))
        self.assertRedirects(response, '/accounts/login/?next=/DeleteProduct/1/')

    def test_redirect_if_not_logged_in_category(self):
        response = self.client.get(reverse('CategoryList'))
        self.assertRedirects(response, '/accounts/login/?next=/CategoryList/')

    def test_redirect_if_not_logged_in_category_create(self):
        response = self.client.get(reverse('CategoryCreate'))
        self.assertRedirects(response, '/accounts/login/?next=/CategoryCreate/')

    def test_redirect_if_not_logged_in_category_update(self):
        response = self.client.get(reverse('CategoryUpdate', kwargs={'pk': self.category.pk}))
        self.assertRedirects(response, '/accounts/login/?next=/CategoryUpdate/1/')

    def test_redirect_if_not_logged_in_category_delete(self):
        response = self.client.get(reverse('DeleteCategory', kwargs={'pk': self.category.pk}))
        self.assertRedirects(response, '/accounts/login/?next=/DeleteCategory/1/')
