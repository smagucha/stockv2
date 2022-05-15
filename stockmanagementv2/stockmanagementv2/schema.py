from goodies.models import Catergory, Product
from sale.models import Sale, Order
import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import  mutations
from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class CatergoryType(DjangoObjectType):
    class Meta:
        model = Catergory
        fields = '__all__'


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = '__all__'


class SaleType(DjangoObjectType):
    class Meta:
        model = Sale
        fields = '__all__'


class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = '__all__'


class Query(UserQuery, MeQuery, graphene.ObjectType):
    all_catergory = graphene.List(CatergoryType)
    all_product = graphene.List(ProductType)
    product = graphene.Field(ProductType, product_id=graphene.Int())
    less_product = graphene.List(ProductType)
    high_stock  = graphene.List(ProductType)
    all_order = graphene.List(OrderType)
    order = graphene.Field(OrderType, order_id=graphene.Int())
    all_sale = graphene.List(SaleType)
    sale = graphene.Field(SaleType, sale_id=graphene.Int())

    def resolve_all_catergory(root, info):
        return Catergory.objects.all()

    def resolve_all_product(root, info):
        return Product.objects.all()

    def resolve_product(root, info, product_id):
        return Product.objects.get(id=product_id)

    def resolve_all_order(root, info):
        return Order.objects.all()

    def resolve_order(root, info, order_id):
        return Order.objects.get(id=order_id)

    def resolve_all_sale(root, info):
        return Sale.objects.all()

    def resolve_sale(root, info, sale_id):
        return Sale.objects.get(id=sale_id)

    def resolve_less_product(root, info):
        return Product.lessquantity.all()

    def resolve_high_product(root,info):
        return Product.quantify.all()


class CreateCatergory(graphene.Mutation):
    id = graphene.ID()
    name = graphene.String()

    class Arguments:
        name = graphene.String()

    def mutate(self, root, name):
        catergory = Catergory(
            name=name
        )
        catergory.save()
        return CreateCatergory(
            id=catergory.id,
            name=Catergory.name,
        )


class UpdateCatergory(graphene.Mutation):
    id = graphene.ID()
    name = graphene.String()

    class Arguments:
        id = graphene.Int()
        name = graphene.String()

    def mutate(root, info, id, name):
        catergory = Catergory.objects.get(pk=id)
        catergory.name = name
        catergory.save()

        return UpdateCatergory(
            id=catergory.id,
            name=catergory.name,
        )


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    catergory = graphene.Field(CatergoryType)

    @staticmethod
    def mutate(root, info, id):
        catergory = Catergory.objects.get(pk=id)
        catergory.delete()
        return None


class CreateProduct(graphene.Mutation):
    id = graphene.ID()
    name = graphene.String()
    productcatergory_id = graphene.Int()
    weight = graphene.String()
    quantity = graphene.Int()

    class Arguments:
        name = graphene.String()
        productcatergory_id = graphene.Int()
        weight = graphene.String()
        quantity = graphene.Int()

    def mutate(self, root, name, productcatergory_id, weight, quantity):
        product = Product(
            name=name,
            productcatergory_id=productcatergory_id,
            weight=weight,
            quantity=quantity
        )
        product.save()
        return CreateProduct(
            id=product.id,
            productcatergory_id=product.productcatergory_id,
            weight=product.weight,
            quantity=product.quantity
        )


class UpdateProduct(graphene.Mutation):
    id = graphene.ID()
    name = graphene.String()
    productcatergory_id = graphene.Int()
    weight = graphene.String()
    quantity = graphene.Int()

    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        productcatergory_id = graphene.Int()
        weight = graphene.String()
        quantity = graphene.Int()

    def mutate(self, root,id, name, productcatergory_id, weight, quantity):
        product = Product.objects.get(pk=id)
        product.name = name
        product.productcatergory_id = productcatergory_id
        product.weight = weight
        product.quantity = quantity
        product.save()
        return UpdateProduct(
            id=product.id,
            name= product.name,
            productcatergory_id=product.productcatergory_id,
            weight=product.weight,
            quantity=product.quantity
        )


class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, id):
        product = Product.objects.get(pk=id)
        product.delete()
        return None


class AddQuantity(graphene.Mutation):
    id = graphene.ID()
    quantity = graphene.Int()

    class Arguments:
        id = graphene.ID()
        quantity = graphene.Int()

    def mutate(self, root,id, quantity):
        product = Product.objects.get(pk=id)
        product.quantity += quantity 
        product.save()
        return AddQuantity(
            quantity = product.quantity
            )



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


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_email = mutations.SwapEmails.Field()


class Mutation(AuthMutation, graphene.ObjectType):
    create_catergory = CreateCatergory.Field()
    update_catergory = UpdateCatergory.Field()
    delete_catergory = DeleteCategory.Field()
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()
    create_order = CreateOrder.Field()
    delete_order = DeleteOrder.Field()
    create_sale = CreateSale.Field()
    update_sale = UpdateSale.Field()
    delete_sale = DeleteSale.Field()
    add_quantity = AddQuantity.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
