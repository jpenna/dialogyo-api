import graphene

from graphql_api.queries import Query # noqa F401

schema = graphene.Schema(query=Query)
