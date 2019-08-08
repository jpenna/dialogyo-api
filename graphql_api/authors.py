from graphene import ObjectType, String, ID, Field


class Author(ObjectType):
    id = ID(required=True)
    name = String(required=True)
    avatar = String(required=True)


class Query(ObjectType):
    author = Field(Author, id=String(required=True))

    def resolve_author(parent, info, id):
        # if id == '123':
        return {
            'id': '123',
            'name': 'Grizzly Bear',
            'avatar': '#984321'
        }
