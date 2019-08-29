from graphene import (ObjectType, String, List, Field,
                      ID, types, NonNull, DateTime)

privacy_description = '''
[] - Private\n
[*] - Public\n
[&] - Friends\n
['id1', 'id2'] - Selected users\n
'''


class Author(ObjectType):
    id = ID(required=True)  # todo is not unique
    # createdAt = DateTime(required=True)
    name = String(required=True)
    avatar = String(required=True)


class Reply(ObjectType):
    id = ID(required=True)
    body = String(required=True)
    author = Field(Author, required=True)
    dyoId = String(required=True,
                   description="Dyo ID which this reply replies.")


class Dyo(ObjectType):
    id = ID(required=True)
    groupId = String(required=True)
    headline = String()
    body = String(description="The content for the post.", required=True)
    tags = List(NonNull(String), required=True)
    privacy = List(NonNull(String), required=True,
                   description=privacy_description)
    createdAt = types.datetime.DateTime(required=True)
    author = NonNull(Author)
    repliesList = List(NonNull(Reply))
    dyosList = List(lambda: NonNull(Dyo))
    parentList = List(NonNull(ID))
