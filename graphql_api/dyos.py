from graphene import (ObjectType, String, List, Field,
                      Int, ID, types, NonNull, Enum)
from graphql_api import authors


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
    # dyosList = List(Dyo)

    def resolve_author(parent, info):
        return authors.Query.resolve_author(None,
                                            info, id=parent['authorId'])


class Query(ObjectType):
    dyo = Field(Dyo, id=String(required=True))
    dyosList = NonNull(List(NonNull(Dyo)))

    def resolve_dyo(parent, info, id):
        return {
            'id': '1298',
            'headline': 'A title',
            'body': 'My content',
            'tags': ['content', 'first'],
            'privacy': 'private',
            'authorId': '123',
            'repliesCount': 2,
            # 'repliesList': REPLIES,
            'dyosCount': 1,
            # 'dyosList': List(Dyo),
        }

    def resolve_dyosList(parent, info):
        return [{
            'id': 'sa123',
            'headline': 'A title',
            'body': 'My content',
            'tags': ['content', 'first'],
            'privacy': 'private',
            # 'author': AUTHOR,
            'repliesCount': 2,
            # 'repliesList': REPLIES,
            'dyosCount': 1,
            # 'dyosList': List(Dyo),
        }]
