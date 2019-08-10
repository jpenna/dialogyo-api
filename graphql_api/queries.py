from graphene import (ObjectType, String, List, Field,
                      ID, types, NonNull)
from graphql_api._data import dyo1, dyo2, reply1, reply2


class Author(ObjectType):
    id = ID(required=True)
    name = String(required=True)
    avatar = String(required=True)


class Reply(ObjectType):
    id = ID(required=True)
    body = String(required=True)
    author = Field(Author, required=True)


privacy_description = '''
[] - Private\n
[*] - Public\n
[&] - Friends\n
['id1', 'id2'] - Selected users\n
'''


class Dyo(ObjectType):
    id = ID
    headline = String(default_value="", required=True)
    body = String(description="The content for the post.", required=True)
    tags = NonNull(List(NonNull(String)))
    privacy = NonNull(List(
                    NonNull(String)), description=privacy_description)
    createdAt = types.datetime.DateTime(required=True)
    author = NonNull(Author)
    repliesList = NonNull(List(NonNull(Reply)))
    dyosList = NonNull(List(lambda: NonNull(Dyo)))


class Query(ObjectType):
    dyo = Field(Dyo, id=String(required=True))
    dyosList = NonNull(List(NonNull(Dyo)))
    reply = Field(Reply, id=String(required=True))
    repliesList = List(Reply)

    def resolve_dyo(parent, info, id):
        return dyo1 if id == '1' else \
               dyo2 if id == '2' else None

    def resolve_dyosList(parent, info):
        return [dyo1, dyo2]

    def resolve_reply(parent, info, id):
        return reply1 if id == '1' else \
                reply2 if id == '2' else None

    def resolve_repliesList(parent, info, id):
        return [reply1, reply2]
