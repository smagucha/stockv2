from graphene_django.utils.testing import GraphQLTestCase
import json
from goodies.models import Product,Catergory

class Test_Product_Catergory(GraphQLTestCase):
	def setUp(self):
		Catergory.objects.create(name='Electronic')
		Product.objects.create(
		name='sams',
		productcatergory_id='1',
		weight='7 kg',
		quantity=100,
	    )

	def test_create_catergory(self):
		response = self.query(
			"""
			mutation($name: String!){
  				createCatergory(name:$name){
    				name
			  }
			}
			""",
			variables = {"name": "stationary"}
			)
		
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)
	
	def test_update_catergory(self):
		response = self.query(
			"""
			mutation($id: Int!,  $name: String){
				updateCatergory(id: $id, name: $name){
		    		id,
		    		name
		 		}
			}
			""",
			variables = {"id":1, "name":"Catergory"}
		)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)
		
	def test_delete_catergory(self):
		response = self.query(
			"""
			mutation($id: ID!){
			 deleteCatergory(id: $id){
			  catergory{
			    id,
			    name
			  }
			}
			}
			""",
			variables ={"id":1}
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)

	def test_create_product(self):
		response = self.query(
			"""
			mutation($name: String!, $productcatergoryId: Int!, $quantity: Int!, $weight: String!){
			  createProduct(name: $name, productcatergoryId:$productcatergoryId, quantity: $quantity,weight:$weight){
			    name,
			    productcatergoryId,
			    quantity,
			    weight
			  }
			}
			""",
			variables = {"name": "samas", "productcatergoryId": 1,"quantity": 200, "weight":"1x9"}
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)
		

	def test_update_product(self):
		response = self.query(
			"""
			mutation($id:Int!, $name: String!, $productcatergoryId: Int!, $quantity: Int!, $weight: String!){
				updateProduct(id:$id,name: $name, productcatergoryId:$productcatergoryId, quantity: $quantity,weight:$weight ){
				  name,
				  productcatergoryId,
				  weight,
				  quantity
				}
			}
			""",
			variables = {"id":1, "name": "samas", "productcatergoryId": 1,"quantity": 200, "weight":"1x9"}
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)


	def test_delete_product(self):
		
		response = self.query(
			"""
			mutation($id: ID!){
			  deleteProduct(id: $id){
			    product{
			    	id,
			    	name,
			    }
			  }
			}
			""",
			variables={"id": 1}
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)
		

	def test_add_quantity(self):
		response = self.query(
			"""
			mutation($id: ID!, $quantity: Int!){
			 addQuantity(id: $id,quantity: $quantity){
			  quantity
			}
			}
			""",
			variables ={"id": 1,"quantity": 500}
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)
		
		


