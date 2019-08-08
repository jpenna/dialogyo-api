from graphene import ObjectType, Field, ID, String, List
from graphql_api import authors

from graphql_api._data import reply1, reply2


class Reply(ObjectType):
    id = ID(required=True)
    body = String(required=True)
    author = Field(authors.Author, required=True)


class Query(ObjectType):
    reply = Field(Reply, id=String(required=True))
    repliesList = List(Reply)

    def resolve_reply(parent, info, id):
        return reply1 if id == '1' else \
               reply2 if id == '2' else None

    def resolve_repliesList(parent, info, id):
        return [reply1, reply2]
