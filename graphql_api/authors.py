from graphene import ObjectType, String, ID


class Author(ObjectType):
    id = ID(required=True)
    name = String(required=True)
    avatar = String(required=True)
