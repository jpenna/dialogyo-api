from graphene import (ObjectType, String, List, Field,
                      ID, types, NonNull)
from graphql_api import authors, replies

from graphql_api._data import dyo1, dyo2

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
    author = NonNull(authors.Author)
    repliesList = NonNull(List(NonNull(replies.Reply)))
    dyosList = NonNull(List(lambda: NonNull(Dyo)))


class Query(ObjectType):
    dyo = Field(Dyo, id=String(required=True))
    dyosList = NonNull(List(NonNull(Dyo)))

    def resolve_dyo(parent, info, id):
        return dyo1 if id == '1' else \
               dyo2 if id == '2' else None

    def resolve_dyosList(parent, info):
        return [dyo1, dyo2]
