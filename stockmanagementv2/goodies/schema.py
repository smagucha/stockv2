import graphene
from graphene_django import DjangoObjectType
from .models import Catergory, Product


class CatergoryType(DjangoObjectType):
    class Meta:
        model = Catergory
        fields = '__all__'


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = '__all__'


class GoodiesQuery(graphene.ObjectType):
    all_catergory = graphene.List(CatergoryType)
    all_product = graphene.List(ProductType)
    product = graphene.Field(ProductType, product_id=graphene.Int())
    less_product = graphene.List(ProductType)
    high_stock = graphene.List(ProductType)

    def resolve_all_catergory(root, info):
        return Catergory.objects.all()

    def resolve_all_product(root, info):
        return Product.objects.all()

    def resolve_product(root, info, product_id):
        return Product.objects.get(id=product_id)

    def resolve_less_product(root, info):
        return Product.lessquantity.all()

    def resolve_high_product(root, info):
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

    def mutate(self, root, id, name, productcatergory_id, weight, quantity):
        product = Product.objects.get(pk=id)
        product.name = name
        product.productcatergory_id = productcatergory_id
        product.weight = weight
        product.quantity = quantity
        product.save()
        return UpdateProduct(
            id=product.id,
            name=product.name,
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

    def mutate(self, root, id, quantity):
        product = Product.objects.get(pk=id)
        product.quantity += quantity
        product.save()
        return AddQuantity(
            quantity=product.quantity
        )


class GoodiesMutation(graphene.ObjectType):
    create_catergory = CreateCatergory.Field()
    update_catergory = UpdateCatergory.Field()
    delete_catergory = DeleteCategory.Field()
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()
    add_quantity = AddQuantity.Field()
