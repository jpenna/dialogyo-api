from graphene import (ObjectType, String, List, Field,
                      Int, ID, types, NonNull, Enum)


class PrivacyEnum(Enum):
    private = 0
    public = 1

    @property
    def description(self):
        if self == PrivacyEnum.private:
            return 'Only the author and the addressee\
                    can view the conversation.'
        return 'Everyone can view the conversation and take part in it.'


class Dyo(ObjectType):
    id: ID
    headline = String(default_value="")
    body = String(description="The content for the post.", required=True)
    tags = List(String)
    privacy = PrivacyEnum(description="The level of privacy set for this dyo.")
    createdAt = types.datetime.DateTime()
    # author = AUTHOR
    repliesCount = Int(required=True)
    # repliesList = REPLIES
    dyosCount = Int(required=True)
    # dyosList = List(Dyo)


class Query(ObjectType):
    dyo = Field(Dyo, id=String(required=True))
    dyosList = NonNull(List(NonNull(Dyo)))

    def resolve_dyo(parent, info, id):
        return {
            'id': '1298',
            'headline': 'A title',
            'body': 'My content',
            'tags': ['content', 'first'],
            'mode': 'private',
            # 'author': AUTHOR,
            'repliesCount': 2,
            # 'repliesList': REPLIES,
            'dyosCount': 1,
            # 'dyosList': List(Dyo),
        }

    def resolve_dyosList(parent, info):
        return [{
            'headline': 'A title',
            'body': 'My content',
            'tags': ['content', 'first'],
            'mode': 'private',
            # 'author': AUTHOR,
            'repliesCount': 2,
            # 'repliesList': REPLIES,
            'dyosCount': 1,
            # 'dyosList': List(Dyo),
        }]
