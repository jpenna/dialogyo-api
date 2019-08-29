import db.dyo as dyoDB
from graphene import ObjectType, String, List, NonNull, Mutation
from client_api.types import Dyo, privacy_description, Reply

from client_api._data import author1, reply1, dyo1


class CreateDyo(Mutation):
    class Arguments:
        parentId = String()
        groupId = String()

        headline = String()
        body = String(description="The content for the post.", required=True)
        tags = List(NonNull(String), required=True,
                    description="Define at least 3 tags.")
        privacy = List(String, default_value=[],
                       description=privacy_description)

    Output = Dyo

    def mutate(root, info, body, tags, privacy, groupId=None, parentId=None,
               headline=''):
        assert len(tags) >= 3, 'Set at least 3 tags'

        userId = '123'
        dyo = {
            'headline': headline,
            'body': body,
            'tags': tags,
            'privacy': privacy,
        }
        author = {
            'name': author1['name'],
            'avatar': author1['avatar'],
        }

        result = dyoDB.create_dyo(userId, dyo, author)
        return Dyo(**result)


class CreateReply(Mutation):
    class Arguments:
        dyoId = String(required=True,
                       description="Dyo ID which this reply replies.")
        body = String(required=True)
        authorId = String(required=False)

    Output = Reply

    def mutate(root, info, dyoId, body, authorId=None):
        reply = {
            'id': 'fwo2',
            'dyoId': dyoId,
            'body': body,
            'author': author1
        }
        return Reply(**reply)


class Mutations(ObjectType):
    create_dyo = CreateDyo.Field()
    add_reply = CreateReply.Field()
