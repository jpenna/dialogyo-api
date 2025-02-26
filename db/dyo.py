import uuid
from db import GraphDB
from app_errors import ApiError


@GraphDB.tx_read
def get_dyo_by_id(tx: callable, dyoId: str):
    statement = """
        MATCH (dyo:Dyo { id: $dyoId })
        RETURN dyo
    """

    result = tx.run(statement, dyoId=dyoId)

    try:
        value = result.data()[0]
    except IndexError:
        raise ApiError(404, 'Not found', 'No Dyo was found with the requested ID.')

    return dict(value['dyo'])


def create_dyo(userId: str, dyo: dict, author: dict):
    """Create Dyo, both head and start new thread.
    It bases the creation of a dyo on the presence of `dyo.parentId`.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    # Create new user ID if not set
    if not userId:
        userId = uuid.uuid4().hex

    callback = _tx_create_dyo if dyo.get('parentId') else _tx_create_head

    return GraphDB.tx_write(callback)(userId, dyo, author)


# TODO use Node for tags, instead of prop
def _tx_create_head(tx: callable, userId: str, dyo: dict, author: dict):
    """Create head Dyo node: starter node of the group

    Attributes:
        tx -- Transaction callback given by neo4j driver
        userId -- Creator user ID
        dyo -- Attributes of the dyo to be created
        author -- Properties of the Author (if creating new author)
    """

    dyoId = uuid.uuid4().hex
    groupId = uuid.uuid4().hex

    statement = """
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
        MERGE (author)-[:MEMBER]->(group:Group { id: $groupId })
        CREATE (author)-[:WROTE]->(dyo:Dyo:Head {
                id: $dyoId,
                createdAt: timestamp(),
                headline: $dyo.headline,
                body: $dyo.body,
                tags: $dyo.tags,
                privacy: $dyo.privacy
            })-[:BELONGS_TO]->(group)
        RETURN dyo{.*, groupId:$groupId},
            author,
            user.id as userId
    """

    result = tx.run(statement, dyo=dyo, author=author,
                    dyoId=dyoId, groupId=groupId, userId=userId)
    values = result.data()[0]

    dyo = values['dyo']
    dyo['author'] = dict(values['author'])

    return dict(
        dyo=dyo,
        userId=values['userId'],
    )


def _tx_create_dyo(tx: callable, userId: str, dyo: dict, author: dict):
    dyoId = uuid.uuid4().hex
    groupId = dyo['groupId']

    statement = """
        MATCH (group:Group { id: $groupId })
        MATCH (parentDyo:Dyo { id: $dyo.parentId })-
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
        CREATE (author)-[:WROTE]->(dyo:Dyo {
                id: $dyoId,
                createdAt: timestamp(),
                body: $dyo.body,
                privacy: $dyo.privacy
            })-[:BELONGS_TO]->(group)
        CREATE (dyo)-[:ENGAGE]->(parentDyo)
        RETURN dyo{.*, groupId:$groupId, parentId:parentDyo.id},
            author,
            user.id as userId
    """

    result = tx.run(statement, dyo=dyo, author=author,
                    dyoId=dyoId, groupId=groupId, userId=userId)

    try:
        values = result.data()[0]
    except IndexError:
        raise ApiError(99, 'UnknownError',
                       'Could not create your Dyo. Maybe the provided `groupId` '
                       'or `parentId` does not exist')

    resDyo = values['dyo']
    resDyo['author'] = dict(values['author'])

    return dict(
        dyo=resDyo,
        userId=values['userId'],
    )
