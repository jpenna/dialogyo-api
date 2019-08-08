from graphene import (ObjectType, String, List, Field,
                      Int, ID, types, NonNull, Enum)
from graphql_api import authors, replies

from graphql_api._data import dyo1, dyo2


class PrivacyEnum(Enum):
    private = 'private'
    public = 'public'

    @property
    def description(self):
        if self == PrivacyEnum.private:
            return 'Only the author and the addressee\
                    can view the conversation.'
        return 'Everyone can view the conversation and take part in it.'


class Dyo(ObjectType):
    id = ID
    headline = String(default_value="", required=True)
    body = String(description="The content for the post.", required=True)
    tags = NonNull(List(String, required=True))
    privacy = PrivacyEnum(required=True,
                          description="The level of privacy set for this dyo.")
    createdAt = types.datetime.DateTime(required=True)
    author = NonNull(authors.Author)
    repliesCount = Int(required=True)
    repliesList = NonNull(List(NonNull(replies.Reply)))
    dyosCount = Int(required=True)
    dyosList = NonNull(List(lambda: NonNull(Dyo)))


class Query(ObjectType):
    dyo = Field(Dyo, id=String(required=True))
    dyosList = NonNull(List(NonNull(Dyo)))

    def resolve_dyo(parent, info, id):
        return dyo1 if id == '1' else \
               dyo2 if id == '2' else None

    def resolve_dyosList(parent, info):
        return [dyo1, dyo2]
