import graphene
from graphql_api import dyos, replies


class Query(dyos.Query, replies.Query):
    pass


schema = graphene.Schema(query=Query)
