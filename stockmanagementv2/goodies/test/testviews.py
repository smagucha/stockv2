from django.test import TestCase
from django.urls import reverse, resolve
from goodies.models import Catergory, Product
from goodies.views import ProductList, ProductCreate, ProductUpdate, DeleteProduct, LowStockProduct, HighStockProduct,AddProductQuantity
from goodies.forms import AddProduct

class Catergory_Test(TestCase):

    def setUp(self):
        Catergory.objects.create(
            name='Electronic'
        )
        self.category = Catergory.objects.get(pk=1)
        self.data = {'name': 'Electronic'}

    def test_catergory_list(self):
        url = reverse('home')
        response = self.client.get(
            reverse('CategoryList')
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resolve(url).func.view_class.__name__, 'ProductList')

    def test_CategoryCreate(self):
        url = reverse('ProductCreate')
        response = self.client.post(
            reverse('ProductCreate'),
            self.data
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resolve(url).func.view_class.__name__, 'ProductCreate')

    def test_category_update(self):
        url = reverse('CategoryUpdate', kwargs={'pk': self.category.pk})
        response = self.client.post(
            reverse(
                'ProductUpdate', kwargs={
                    'pk': self.category.pk
                }
            ),
            self.data
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resolve(url).func.view_class.__name__, 'CategoryUpdate')

    def test_delete_category(self):
        url = reverse('DeleteCategory', kwargs={'pk': self.category.pk})
        response = self.client.delete(
            reverse(
                'DeleteProduct', kwargs={
                    'pk': self.category.pk
                }
            ),
            self.data
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(resolve(url).func.view_class.__name__, 'DeleteCategory')


class ProductTest(TestCase):

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
        self.data = {
            'name': 'samsung tv',
            'productcatergory_id': 1,
            'weight': '7 kg',
            'quantity': 100,
        }

    def test_ProductList(self):
        url = reverse('home')
        response = self.client.get(reverse('home'))
        self.assertEqual(
            response.status_code, 302
        )
        self.assertEqual(resolve(url).func.view_class.__name__, 'ProductList')

    def test_ProductCreate(self):
        url = reverse('ProductCreate')
        response = self.client.post(
            reverse('ProductCreate'),
            self.data
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertEqual(resolve(url).func.view_class.__name__, 'ProductCreate')

    def test_ProductUpdate(self):
        url = reverse('ProductUpdate', kwargs={'pk': self.product.pk})
        response = self.client.post(
            reverse(
                'ProductUpdate',
                kwargs={'pk': self.product.pk}
            ),
            self.data
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertEqual(resolve(url).func.view_class.__name__, 'ProductUpdate')

    def test_DeleteProduct(self):
        url = reverse('DeleteProduct', kwargs={'pk': self.product.pk})
        response = self.client.post(
            reverse(
                'DeleteProduct',
                kwargs={'pk': self.product.pk}
            ),
            self.data
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertEqual(resolve(url).func.view_class.__name__, 'DeleteProduct')

    def test_get_context_data(self):
        response = self.client.get(reverse('home'))
        view = ProductList()
        view.setup(response)
        view.object_list = view.get_queryset()
        context = view.get_context_data()
        self.assertEqual(context['page_title'], 'home page')

    def test_get_context_data_low_stock(self):
        response = self.client.get(reverse('less_stock'))
        view = LowStockProduct()
        view.setup(response)
        view.object_list = view.get_queryset()
        context = view.get_context_data()
        self.assertEqual(context['page_title'], 'low stock')

    def test_get_context_data_high_stock(self):
        response = self.client.get(reverse('highstock'))
        view = HighStockProduct()
        view.setup(response)
        view.object_list = view.get_queryset()
        context = view.get_context_data()
        self.assertEqual(context['page_title'], 'High stock')

    def test_sale_pdf_view_post(self):
        response = self.client.get(
            reverse('SalePdfView'),
        )
        self.assertEqual(response.status_code, 200)

    def test_render_view_sale(self):
        start_date = '2022-03-27'
        end_date = '2022-04-15'
        response = self.client.get(reverse('render_pdf_view', kwargs={'start_date': start_date, 'end_date': end_date}))
        self.assertEqual(response.status_code, 200)
        url = reverse('render_pdf_view', kwargs={'start_date': start_date, 'end_date': end_date})
        self.assertEqual(resolve(url).func.__name__, 'render_pdf_view')

    def test_sale_pdf_view(self):
        start_date = '2022-03-27'
        end_date = '2022-04-15'
        response = self.client.post(
            reverse('SalePdfView'),
            {
                'start_date': start_date,
                'end_date': end_date,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/render_pdf_view/2022-03-27/2022-04-15')

    def test_get_add_product_quantity(self):
        response = self.client.get(reverse('AddProductQuantity', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 302)
        view = AddProductQuantity()
        print(view.__dict__)
        



