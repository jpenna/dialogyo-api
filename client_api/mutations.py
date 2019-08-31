import db.dyo as dyoDB
from operator import xor
from ariadne import MutationType

from client_api._data import author1, author2

mutation = MutationType()


@mutation.field('createDyo')
def resolve_create_dyo(_, info, body, tags, privacy=['*'], groupId='',
                       parentId='', headline=''):
    if len(tags) < 3:
        raise ValueError('Set at least 3 tags.')
    if len(body) < 1:
        raise ValueError('Set a body.')
    if xor(bool(groupId), bool(parentId)):
        raise ValueError('To start a dialogue, please set both `parentId` and '
                         '`groupId`. Otherwise, leave both empty to create a new Dyo.')

    userId = headline  # get from cookie
    authorData = author1  # get from Redis

    dyo = dict(headline=headline, body=body, tags=tags, privacy=privacy,
               parentId=parentId, groupId=groupId)
    author = dict(name=authorData['name'], avatar=authorData['avatar'])

    return dyoDB.create_dyo(userId, dyo, author)



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
