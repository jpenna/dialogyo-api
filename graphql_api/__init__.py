import graphene

from graphql_api.mutations import Mutations # noqa F401
from graphql_api.queries import Query # noqa F401

schema = graphene.Schema(query=Query, mutation=Mutations)
