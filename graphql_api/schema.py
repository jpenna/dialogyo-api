import graphene
from graphql_api import dyos, authors


class Query(dyos.Query, authors.Query):
    pass


schema = graphene.Schema(query=Query)
