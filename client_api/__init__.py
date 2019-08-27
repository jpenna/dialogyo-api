import graphene

from client_api.mutations import Mutations # noqa F401
from client_api.queries import Query # noqa F401

schema = graphene.Schema(query=Query, mutation=Mutations)
