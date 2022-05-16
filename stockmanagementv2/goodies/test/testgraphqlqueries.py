from graphene_django.utils.testing import GraphQLTestCase
import json
from goodies.models import Product,Catergory


class ProductCategoryTestCase(GraphQLTestCase):
	def setUp(self):
		Catergory.objects.create(name='Electronic')
		Product.objects.create(
		name='samsung tv',
		productcatergory_id='1',
		weight='7 kg',
		quantity=100,
	    )

	def test_product_queries(self):
		response = self.query(
			'''
			query{
			allProduct{
				name,
				productcatergory{
				  name
				}
				lastUpdate
				dateCreated,
				id,
				weight
				quantity
				}
				}
	        '''
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)
		

	def test_catergory_queries(self):
		response =self.query(
			"""
			query{
			allCatergory{
			name
			}
			}
			""",
		)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)
		