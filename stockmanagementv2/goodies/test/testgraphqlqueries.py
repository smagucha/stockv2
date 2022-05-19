from graphene_django.utils.testing import GraphQLTestCase
import json
from goodies.models import Product,Catergory


class ProductCategoryTestCase(GraphQLTestCase):
	def setUp(self):
		Catergory.objects.create(name='Electronic')
		Catergory.objects.create(name='stationary')
		Product.objects.create(
		name='samsung tv',
		productcatergory_id='1',
		weight='7 kg',
		quantity=100,
	    )
		Product.objects.create(
		name='books',
		productcatergory_id='2',
		weight='25 kg',
		quantity=1000,
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
			"""
		)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)
	
	def test_product(self):
		response =self.query(
			"""
			query{
			  product(productId: 1){
			    id,
				name,
				productcatergory{
				  id
				},
				weight,
				quantity,
				dateCreated,
				lastUpdate
			  }
			}
			"""
		)
		# variables ={'productId':1}
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)

	def test_high_product_queries(self):
		response = self.query(
			'''
			query{
				highStock{
					name,
					quantity,
					lastUpdate,
					dateCreated,
					productcatergory{
						name
					}
				}
			}
	        '''
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)

	def test_low_product_queries(self):
		response = self.query(
			'''
			query{
				lessProduct{
					name,
					quantity,
					lastUpdate,
					dateCreated,
					productcatergory{
						name
					}
				}
			}
	        '''
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)
