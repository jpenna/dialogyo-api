import graphene
from graphql_api import queries


class Query(queries.Query):
    pass


schema = graphene.Schema(query=Query)
