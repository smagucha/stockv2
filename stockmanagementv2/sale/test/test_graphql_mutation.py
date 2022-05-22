from graphene_django.utils.testing import GraphQLTestCase
import json
from sale.models import Sale,Order
from django.contrib.auth.models import User
from goodies.models import Product, Catergory



class SaleOrderMutationTest(GraphQLTestCase):

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
		User.objects.create(username ='newuser', password='password')
		Sale.objects.create(serverby_id=1,buyer='sam',buyercontact=123531,clientemail="am@sfh.com",item_id=1, quantity=100)
		Order.objects.create(buyer="sam", email="sma@sa.com",phonenumber=12345,product_id=1, quantity=100)

	def test_create_sale(self):
		response = self.query(
			"""
			mutation($serverbyId:Int!,$itemId:Int!,$buyer:String!,$quantity: Int!, $clientemail:String!,$buyercontact:Int! ){
			  createSale(
			  	serverbyId:$serverbyId,
			  	itemId:$itemId,
			  	buyer:$buyer,
			  	quantity:$quantity,
			  	clientemail:$clientemail, 
			  	buyercontact:$buyercontact
			  	){
				    serverbyId,
				    buyer,
				    buyercontact,
				    itemId,
				    quantity
			  }
			}
			""",
			variables = {"serverbyId":1,"buyer":"sam","buyercontact":1235,"clientemail":"sa@sa.cm","itemId":1,"quantity":200}
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)
	
	def test_update_sale(self):
		response = self.query(
			"""
			mutation($id: ID!, $serverbyId:Int!,$itemId:Int!,$buyer:String!,$quantity: Int!, $clientemail:String!,$buyercontact:Int! ){
			  updateSale(
			  	id: $id,
			  	serverbyId:$serverbyId,
			  	itemId:$itemId,
			  	buyer:$buyer,
			  	quantity:$quantity,
			  	clientemail:$clientemail, 
			  	buyercontact:$buyercontact
			  	){
				    serverbyId,
				    buyer,
				    buyercontact,
				    itemId,
				    quantity
			  }
			}
			""",
			variables = {"id":1, "serverbyId":1,"buyer":"sam","buyercontact":1235,"clientemail":"sa@sa.cm","itemId":1,"quantity":5800}
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)


	def test_delete_catergory(self):
		response = self.query(
			"""
			mutation($id: ID!){
			 deleteSale(id: $id){
			  saleInstance{
				buyer
				}
			}
			}
			""",
			variables ={"id":1}
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)
		

	def test_create_order(self):
		response = self.query(
			"""
			mutation($buyer: String!, $email: String!, $phonenumber:Int!, $productId:Int!,  $quantity:Int!){
			  createOrder(buyer:$buyer, email:$email, phonenumber:$phonenumber,productId:$productId,quantity:$quantity){
			    buyer,
			    email,
			    phonenumber,
			    productId,
			    quantity
			  }
			}
			""",
			variables ={"buyer":"sam", "email":"sam@d.com", "phonenumber":12345,"productId":1,"quantity":100}
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)

	def test_delete_sale(self):
		response = self.query(
			"""
			mutation($id: ID){
			  deleteSale(id:$id){
			    saleInstance{
			      buyer
			    }
			  }
			}
			""",
			variables ={"id":1}
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)
