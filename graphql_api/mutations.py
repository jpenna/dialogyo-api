import datetime
from graphene import ObjectType, String, List, NonNull, Mutation
from graphql_api.types import Dyo, privacy_description, Reply

from graphql_api._data import author1, reply1, dyo1


class CreateDyo(Mutation):
    class Arguments:
        authorId = String()
        parentId = String()

        headline = String()
        body = String(description="The content for the post.", required=True)
        tags = List(NonNull(String), required=True,
                    description="Define at least 3 tags.")
        privacy = List(String, default_value=[],
                       description=privacy_description)

    Output = Dyo

    def mutate(root, info, body, tags, privacy, parentId=None, authorId=None,
               headline=''):
        assert len(tags) >= 3, 'Set at least 3 tags'
        dyo = {
            'id': '1234asd',
            'headline': headline,
            'body': body,
            'tags': tags,
            'createdAt': datetime.datetime.now(),
            'privacy': privacy,
            'author': author1,
            'repliesList': [reply1],
            'dyosList': [dyo1]
        }
        return Dyo(**dyo)


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
