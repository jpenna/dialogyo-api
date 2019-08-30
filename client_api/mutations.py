import db.dyo as dyoDB
from graphene import ObjectType, String, List, NonNull, Mutation, Field
from client_api.types import Dyo, privacy_description, Reply
from client_api.db_handler import dispatch_db

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

    dyo = Field(lambda: Dyo)
    userId = String(required=True)

    def mutate(root, info, body, tags, privacy, groupId=None, parentId=None,
               headline=''):
        assert len(tags) >= 3, 'Set at least 3 tags'

        userId = 'another'
        dyo = dict(
            headline=headline,
            body=body,
            tags=tags,
            privacy=privacy,
            parentId=parentId,
            groupId=groupId,
        )
        author = dict(
            name=author1['name'],
            avatar=author1['avatar'],
        )

        result = dispatch_db(dyoDB.create_dyo, userId, dyo, author)
        resDyo = result['dyo']
        resAuthor = result['author']

        newAuthor = dict(
            id='whatever',
            name=resAuthor.get('name', ''),
            avatar=resAuthor.get('avatar', ''),
        )
        newDyo = Dyo(**dict(
            id=resDyo.get('id', ''),
            groupId=resDyo.get('groupId', ''),
            headline=resDyo.get('headline', ''),
            body=resDyo.get('body', ''),
            tags=resDyo.get('tags', []),
            createdAt=str(resDyo.get('createdAt', '')),
            privacy=resDyo.get('privacy', []),
            author=newAuthor,
            repliesList=resDyo.get('repliesList', []),
            dyosList=resDyo.get('dyosList', []),
            parentList=resDyo.get('parentList', []),
        ))
        return CreateDyo(dyo=newDyo, userId=result['userId'])


class CreateReply(Mutation):
    class Arguments:
        dyoId = String(required=True,
                       description="Dyo ID which this reply replies.")
        body = String(required=True)
        authorId = String(required=False)

    Output = Reply

    def mutate(root, info, dyoId, body, authorId=None):
        reply = dict(
            id='fwo2',
            dyoId=dyoId,
            body=body,
            author=author1
        )
        return Reply(**reply)


class Mutations(ObjectType):
    create_dyo = CreateDyo.Field()
    add_reply = CreateReply.Field()
