import uuid
from db import GraphDB

from client_api._data import author1, reply1, dyo1


def create_dyo(userId, dyo, author):
    # Create new user ID if not set
    if not userId:
        userId = uuid.uuid4().hex

    with GraphDB._driver.session() as session:
        dyo = session.write_transaction(
            _tx_create_dyo,
            userId,
            dyo,
            author,
        )
        return dyo


def _tx_create_dyo(tx, userId, dyo, author):
    dyoId = uuid.uuid4().hex
    groupId = dyo.get('groupId', dyoId)

    statement = """
        MERGE (user:User { userId: $userId })
            ON CREATE SET
                user:Loose,
                user.createdAt = timestamp(),
                user.lastAccess = timestamp()
            ON MATCH SET
                user.lastAccess = timestamp()
        MERGE (user)-[rel:IS]->
                (author:Author { groupId: $groupId })
            ON CREATE SET
                author.createdAt = timestamp(),
                author.name = $author.name,
                author.avatar = $author.avatar
        CREATE (author)-[:WROTE]->(dyo:Dyo {
            id: $dyoId,
            groupId: $groupId,
            createdAt: timestamp(),
            headline: $dyo.headline,
            body: $dyo.body,
            tags: $dyo.tags,
            privacy: $dyo.privacy
        })
        RETURN dyo
    """

    result = tx.run(statement, dyo=dyo, author=author,
                    dyoId=dyoId, groupId=groupId, userId=userId)
    # values = result.single().value()
    # tx.commit()
    return {
        'id': '1234asd',
        'headline': dyo['headline'],
        'body': dyo['body'],
        'tags': dyo['tags'],
        'createdAt': '123412312',
        'privacy': dyo['privacy'],
        'author': author1,
        'repliesList': [reply1],
        'dyosList': [dyo1]
    }
