import db.dyo as dyoDB
from ariadne import MutationType

from client_api._data import author1, reply1, dyo1

mutation = MutationType()


@mutation.field("createDyo")
def resolve_create_dyo(_, info, body, tags, privacy=[], headline=''):
    assert len(tags) >= 3, 'Set at least 3 tags'

    userId = 'another'
    authorData = author1  # get from Redis

    dyo = dict(headline=headline, body=body, tags=tags, privacy=privacy)
    author = dict(name=authorData['name'], avatar=authorData['avatar'])

    result = dyoDB.create_dyo(userId, dyo, author)
    resDyo = result['dyo']
    resAuthor = result['author']

    return {}

        # newAuthor = dict(
        #     id='whatever',
        #     name=resAuthor.get('name', ''),
        #     avatar=resAuthor.get('avatar', ''),
        # )
        # newDyo = Dyo(**dict(
        #     id=resDyo.get('id', ''),
        #     groupId=resDyo.get('groupId', ''),
        #     headline=resDyo.get('headline', ''),
        #     body=resDyo.get('body', ''),
        #     tags=resDyo.get('tags', []),
        #     createdAt=str(resDyo.get('createdAt', '')),
        #     privacy=resDyo.get('privacy', []),
        #     author=newAuthor,
        #     repliesList=resDyo.get('repliesList', []),
        #     dyosList=resDyo.get('dyosList', []),
        #     parentList=resDyo.get('parentList', []),
        # ))
        # return (dyo=newDyo, userId=result['userId'])


# class CreateReply(Mutation):
#     class Arguments:
#         dyoId = String(required=True,
#                        description="Dyo ID which this reply replies.")
#         body = String(required=True)
#         authorId = String(required=False)

#     Output = Reply

#     def mutate(root, info, dyoId, body, authorId=None):
#         reply = dict(
#             id='fwo2',
#             dyoId=dyoId,
#             body=body,
#             author=author1
#         )
#         return Reply(**reply)


# class Mutations(ObjectType):
#     create_dyo = CreateDyo.Field()
#     add_reply = CreateReply.Field()
