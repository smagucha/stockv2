from goodies.models import Catergory, Product
from sale.models import Sale, Order
import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import  mutations
from goodies.schema import GoodiesQuery, GoodiesMutation
from sale.schema import SaleQuery, SaleMutation


class Query(GoodiesQuery, SaleQuery, UserQuery, MeQuery, graphene.ObjectType):
    pass


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


class Mutation(GoodiesMutation, SaleMutation, AuthMutation, graphene.ObjectType):
    pass
    

schema = graphene.Schema(query=Query, mutation=Mutation)
