import uuid
from db import GraphDB
from app_errors import ApiError


@GraphDB.tx_write
def create_reply(tx: callable, userId: str, reply: dict, author: dict):
    replyId = uuid.uuid4().hex
    groupId = reply['groupId']
    dyoId = reply['dyoId']

    # Create new user ID if not set
    if not userId:
        userId = uuid.uuid4().hex

    statement = """
        MATCH (group:Group { id: $groupId })
        MATCH (dyo:Dyo { id: $reply.dyoId })-
            [:BELONGS_TO]->(group)
        MERGE (user:User { id: $userId })
            ON CREATE SET
                user:Loose,
                user.createdAt = timestamp(),
                user.lastAccess = timestamp()
        MERGE (author:Author)<-[rel:IS { groupId: $groupId }]-(user)
            ON CREATE SET
                rel.createdAt = timestamp(),
                author.name = $author.name,
                author.avatar = $author.avatar
        SET rel.lastOp = timestamp()
        MERGE (author)-[:MEMBER]->(group)
        CREATE (author)-[:WROTE]->(reply:Reply {
                id: $replyId,
                dyoId: $dyoId,
                createdAt: timestamp(),
                private: $reply.private,
                body: $reply.body
            })-[:BELONGS_TO]->(group)
        CREATE (reply)-[:REPLIES]->(dyo)
        RETURN reply{.*, groupId:$groupId, dyoId:$dyoId},
            author,
            user.id as userId
    """

    result = tx.run(statement, reply=reply, replyId=replyId, author=author,
                    dyoId=dyoId, groupId=groupId, userId=userId)

    try:
        values = result.data()[0]
    except IndexError:
        raise ApiError(99, 'UnknownError',
                       'Could not create your Dyo. Maybe the provided `groupId` '
                       'or `dyoId` does not exist')

    resReply = values['reply']
    resReply['author'] = dict(values['author'])

    return dict(
        reply=resReply,
        userId=values['userId'],
    )
