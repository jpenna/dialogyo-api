import db.dyo as dyoDB
import db.reply as replyDB
from operator import xor
from ariadne import MutationType
from app_errors import ApiError

from client_api._data import author1

mutation = MutationType()


@mutation.field('createDyo')
def resolve_create_dyo(_, info, body: str, tags: list, headline: str = '',
                       privacy: list = ['*'], groupId: str = '', parentId: str = ''):
    """Create a new base dyo or an dyo that starts a dialogue
    Arguments
        body -- (base/engage) -- Content of the reply
        headline -- (base) -- Headline for the Dyo
        tags -- (base) -- List of tags for this Dyo (only for base dyos)
        groupId -- (engage) -- Group ID of the parent Dyo if starting dialogue
        parentId -- (engage) -- Dyo ID of the parent Dyo if starting dialogue
    """

    if len(tags) < 3:
        raise ApiError(1, 'InvalidValue', 'Set at least 3 tags.')
    if len(body) < 1:
        raise ApiError(1, 'InvalidValue', 'Set a body.')
    if xor(bool(groupId), bool(parentId)):
        raise ApiError(1, 'InvalidValue', 'To start a dialogue, please set both `parentId` and '
                       '`groupId`. Otherwise, leave both empty to create a new Dyo.')

    userId = headline  # get from cookie
    authorData = author1  # get from Redis

    dyo = dict(headline=headline, body=body, tags=tags, privacy=privacy,
               parentId=parentId, groupId=groupId)
    author = dict(name=authorData['name'], avatar=authorData['avatar'])

    return dyoDB.create_dyo(userId, dyo, author)


@mutation.field('createReply')
def resolve_create_reply(_, info, groupId: str, dyoId: str, body: str, private: bool = False):
    """Create new reply based on the dyoId given
    Arguments
        groupId -- Group ID of the base Dyo
        dyoId -- Dyo ID this reply is replying to
        body -- Content of the reply
        private -- If the reply is visible only for the creator
    """

    if len(body) < 5:
        raise ApiError(5, 'InvalidValue', 'Set a body longer than 5 characters.')
    if xor(bool(groupId), bool(dyoId)):
        raise ApiError(1, 'InvalidValue', 'Please set both `dyoId` and `groupId` '
                       'to create a reply.')

    userId = body  # get from cookie
    authorData = author1  # get from Redis

    reply = dict(body=body, private=private, groupId=groupId, dyoId=dyoId)
    author = dict(name=authorData['name'], avatar=authorData['avatar'])

    return replyDB.create_reply(userId, reply, author)
