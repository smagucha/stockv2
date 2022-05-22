from graphene_django.utils.testing import GraphQLTestCase
import json
from sale.models import Sale,Order
from django.contrib.auth.models import User
from goodies.models import Product, Catergory


class Test_Sale_Order(GraphQLTestCase):

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

	def test_sale_query(self):
		response = self.query(
			"""
			query{
			  allSale{
			    serverby{
			      username
			    },
			    item{
			      name
			      }
			    quantity,
			    clientemail,
			    buyer
			  }
			}
			"""
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)

	def test_single_sale_query(self):
		response = self.query(
			"""
			query($saleId: Int!){
			  sale(saleId:$saleId){
			    serverby{
			      username
			    }
			    item{
			      name
			    }
			    quantity
			    clientemail
			    buyer
			    buyercontact
			  }
			}
			""",
			variables ={"saleId":1}
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)

	def test_all_order(self):
		response = self.query(
			"""
			query{
			  allOrder{
			    buyer
			    email
			    phonenumber
			    product{
			      name
			    }
			    quantity
			  }
			}
			"""
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)
	
	def test_order(self):
		response = self.query(
			"""
			query($orderId: Int!){
			order(orderId:$orderId){
			  buyer
				email
				phonenumber
				product{
			    name
				}
			quantity
			}
			}
			""",
			variables ={'orderId':1}
			)
		content = json.loads(response.content)
		self.assertResponseNoErrors(response)






