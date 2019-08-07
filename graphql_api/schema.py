import graphene
import graphql_api.dyos


class Query(graphql_api.dyos.Query):
    pass


schema = graphene.Schema(query=Query)
