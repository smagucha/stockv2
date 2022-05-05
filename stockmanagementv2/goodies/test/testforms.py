from django.test import SimpleTestCase
from goodies.forms import AddProduct, GeeksForm


class FormTest(SimpleTestCase):

    def test_add_product_form_with_data(self):
        form = AddProduct(
            data={
                'add_quantity': 7,
            }
        )
        self.assertTrue(form.is_valid())

    def test_add_product_form_with_no_data(self):
        form = AddProduct(
            data={}
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_add_date_form_with_data(self):
        form = GeeksForm(
            data={
                'start_date': '04/05/2022',
                'end_date': '12/30/2022',
            }
        )
        self.assertTrue(form.is_valid())

    def test_add_date_form_with_no_data(self):
        form = GeeksForm(
            data={}
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)



