from graphene import (ObjectType, String, List, Field,
                      Int, ID, types, NonNull, Enum)
from graphql_api import authors, _data


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
    headline = String(default_value="")
    body = String(description="The content for the post.", required=True)
    tags = List(String)
    privacy = PrivacyEnum(required=True,
                          description="The level of privacy set for this dyo.")
    createdAt = types.datetime.DateTime(required=True)
    author = Field(authors.Author)
    repliesCount = Int(required=True)
    # repliesList = REPLIES
    dyosCount = Int(required=True)
    dyosList = List(lambda: Dyo)

    def resolve_author(parent, info):
        return authors.Query.resolve_author(None,
                                            info, id=parent['authorId'])


class Query(ObjectType):
    dyo = Field(Dyo, id=String(required=True))
    dyosList = NonNull(List(NonNull(Dyo)))

    def resolve_dyo(parent, info, id):
        return _data.dyo1 if id == '1' else _data.dyo2 if id == '2' else None

    def resolve_dyosList(parent, info):
        return [_data.dyo1, _data.dyo2]
