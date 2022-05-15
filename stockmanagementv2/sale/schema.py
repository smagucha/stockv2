import graphene
from graphene_django import DjangoObjectType
from .models import Sale, Order
from django.contrib.auth.models import User



class UserType(DjangoObjectType):
	class Meta:
		model = User


class SaleType(DjangoObjectType):
	class Meta:
		model = Sale
		fields = '__all__'


class OrderType(DjangoObjectType):
	class Meta:
		model = Order
		fields = '__all__'



class SaleQuery(graphene.ObjectType):
	all_order = graphene.List(OrderType)
	order = graphene.Field(OrderType, order_id=graphene.Int())
	all_sale = graphene.List(SaleType)
	sale = graphene.Field(SaleType, sale_id=graphene.Int())

	def resolve_all_order(root, info):
		return Order.objects.all()

	def resolve_order(root, info, order_id):
		return Order.objects.get(id=order_id)

	def resolve_all_sale(root, info):
		return Sale.objects.all()

	def resolve_sale(root, info, sale_id):
		return Sale.objects.get(id=sale_id)


class CreateOrder(graphene.Mutation):
	id = graphene.ID()
	buyer = graphene.String()
	email = graphene.String()
	phonenumber = graphene.Int()
	product_id = graphene.Int()
	quantity = graphene.Int()

	class Arguments:
			buyer = graphene.String()
			email = graphene.String()
			phonenumber = graphene.Int()
			product_id = graphene.Int()
			quantity = graphene.Int()

	def mutate(self, root, buyer, email, phonenumber, product_id, quantity):
		order = Order(
		buyer=buyer,
		email=email,
		phonenumber=phonenumber,
		product_id=product_id,
		quantity=quantity
		)
		order.save()
		return CreateOrder(
			id=order.id,
			buyer=order.buyer,
			email=order.email,
			phonenumber=order.phonenumber,
			product_id=order.product_id,
			quantity=order.quantity
		)


class DeleteOrder(graphene.Mutation):
	class Arguments:
		id = graphene.ID()

	order = graphene.Field(OrderType)

	@staticmethod
	def mutate(root, info, id):
		order = Order.objects.get(pk=id)
		order.delete()
		return None


class CreateSale(graphene.Mutation):
	id = graphene.ID()
	serverby_id = graphene.Int()
	buyer = graphene.String()
	buyercontact = graphene.Int()
	clientemail = graphene.String()
	item_id = graphene.Int()
	quantity = graphene.Int()

	class Arguments:
		serverby_id = graphene.Int()
		buyer = graphene.String()
		buyercontact = graphene.Int()
		clientemail = graphene.String()
		item_id = graphene.Int()
		quantity = graphene.Int()

	def mutate(self, root, serverby_id, buyer, buyercontact, clientemail, item_id, quantity):
		sale = Sale(
			serverby_id=serverby_id,
			buyer=buyer,
			buyercontact=buyercontact,
			clientemail=clientemail,
			item_id=item_id,
			quantity=quantity,
		)
		sale.save()
		return CreateSale(
			id=sale.id,
			serverby_id=sale.serverby_id,
			buyer=sale.buyer,
			buyercontact=sale.buyercontact,
			clientemail=sale.clientemail,
			item_id=sale.item_id,
			quantity=sale.quantity
		)



class UpdateSale(graphene.Mutation):
	id = graphene.ID()
	serverby_id = graphene.Int()
	buyer = graphene.String()
	buyercontact = graphene.Int()
	clientemail = graphene.String()
	item_id = graphene.Int()
	quantity = graphene.Int()

	class Arguments:
		id = graphene.ID()
		serverby_id = graphene.Int()
		buyer = graphene.String()
		buyercontact = graphene.Int()
		clientemail = graphene.String()
		item_id = graphene.Int()
		quantity = graphene.Int()

	def mutate(self, root, id, serverby_id, buyer, buyercontact, clientemail, item_id, quantity):
		sale = Sale.objects.get(id=id)
		sale.serverby_id = serverby_id
		sale.buyer = buyer
		sale.buyercontact = buyercontact
		sale.clientemail = clientemail
		sale.item_id = item_id
		sale.quantity = quantity
		sale.save()

		return UpdateSale(
			id=sale.id,
			serverby_id=sale.serverby_id,
			buyer=sale.buyer,
			buyercontact=sale.buyercontact,
			clientemail=sale.clientemail,
			item_id=sale.item_id,
			quantity=sale.quantity
		)


class DeleteSale(graphene.Mutation):
	class Arguments:
		id = graphene.ID()

	sale_instance = graphene.Field(SaleType)

	@staticmethod
	def mutate(root, info, id):
		sale = Sale.objects.get(pk=id)
		sale.delete()
		return None

class SaleMutation(graphene.ObjectType):
	create_order = CreateOrder.Field()
	delete_order = DeleteOrder.Field()
	create_sale = CreateSale.Field()
	update_sale = UpdateSale.Field()
	delete_sale = DeleteSale.Field()
