'''for graphql'''

from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
import graphene

UserModel = get_user_model()

class User(DjangoObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return UserModel.objects.all()

schema = graphene.Schema(query=Query)
