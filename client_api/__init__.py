import graphene

from client_api.mutations import Mutations
from client_api.queries import Query

schema = graphene.Schema(query=Query, mutation=Mutations)
