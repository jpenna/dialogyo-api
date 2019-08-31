import uuid
from db import GraphDB


def create_dyo(userId, dyo, author):
    # Create new user ID if not set
    if not userId:
        userId = uuid.uuid4().hex

    callback = _tx_create_dyo if dyo.get('parentId') else _tx_create_head

    return GraphDB.tx_write(callback, userId, dyo, author)


# TODO use Node for tags, instead of prop
def _tx_create_head(tx, userId, dyo, author):
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
            })<-[:CONTAINS]-(group)
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


def _tx_create_dyo(tx, userId, dyo, author):
    dyoId = uuid.uuid4().hex
    groupId = dyo['groupId']

    statement = """
        MATCH (group:Group { id: $groupId })
        MATCH (parentDyo:Dyo { id: $dyo.parentId })<-
            [:CONTAINS]-(group)
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
            })<-[:CONTAINS]-(group)
        CREATE (dyo)-[:ENGAGE]->(parentDyo)
        RETURN dyo{.*, groupId:$groupId, parentId:parentDyo.id},
            author,
            user.id as userId
    """

    result = tx.run(statement, dyo=dyo, author=author,
                    dyoId=dyoId, groupId=groupId, userId=userId)

    try:
        values = result.data()[0]
    except ValueError:
        raise ValueError('Could not create your Dyo. '
                         'Maybe the provided `groupId` or `parentId` does not exist')

    dyo = values['dyo']
    dyo['author'] = dict(values['author'])

    return dict(
        dyo=dyo,
        userId=values['userId'],
    )
