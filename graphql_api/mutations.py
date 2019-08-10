import datetime
from graphene import ObjectType, String, List, NonNull, Mutation
from graphql_api.types import Dyo, privacy_description

from graphql_api._data import author1, reply1, dyo1


class CreateDyo(Mutation):
    class Arguments:
        authorId = String(default_value="")

        headline = String(default_value="")
        body = String(description="The content for the post.", required=True)
        tags = NonNull(List(NonNull(String)),
                       description="Define at least 3 tags.")
        privacy = List(String, default_value=[],
                       description=privacy_description)

    Output = Dyo

    def mutate(root, info, authorId, headline, body, tags, privacy):
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


class Mutations(ObjectType):
    create_dyo = CreateDyo.Field()
