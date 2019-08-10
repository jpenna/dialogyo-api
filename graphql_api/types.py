from graphene import (ObjectType, String, List, Field,
                      ID, types, NonNull)

privacy_description = '''
[] - Private\n
[*] - Public\n
[&] - Friends\n
['id1', 'id2'] - Selected users\n
'''


class Author(ObjectType):
    id = ID(required=True)
    name = String(required=True)
    avatar = String(required=True)


class Reply(ObjectType):
    id = ID(required=True)
    body = String(required=True)
    author = Field(Author, required=True)


class Dyo(ObjectType):
    id = ID(required=True)
    headline = String(default_value="", required=True)
    body = String(description="The content for the post.", required=True)
    tags = NonNull(List(NonNull(String)))
    privacy = NonNull(List(
                    NonNull(String)), description=privacy_description)
    createdAt = types.datetime.DateTime(required=True)
    author = NonNull(Author)
    repliesList = NonNull(List(NonNull(Reply)))
    dyosList = NonNull(List(lambda: NonNull(Dyo)))
