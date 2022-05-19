from graphene_django.utils.testing import GraphQLTestCase
import json
from goodies.models import Product,Catergory

class Test_Product_Catergory(GraphQLTestCase):

	def test_create_catergory(self):
		response = self.query(
			"""
			mutation{
  				createCatergory(name:"stationary"){
    				name
			  }
			}
			"""
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)
		print(response.content)

	def test_create_product(self):
		response = self.query(
			"""
			mutation{
			  createProduct(name:"samas", productcatergoryId:3, quantity:200,weight:"1x9"){
			    name,
			    productcatergoryId,
			    quantity,
			    weight
			  }
			}
			"""
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)
		print(response.content)