MATCH (baseDyo:Dyo { id: $baseDyoId })
MATCH (parentDyo:Dyo { id: $parentDyoId })
MATCH (author:Author { baseId: $baseId })
MERGE (user:User { id: $userId })-[rel:IS]-(author:Author { baseId: $baseId })
	ON CREATE n.created = timestamp()
ON MATCH SET

(author)-[:WRITES]->(dyo:Dyo)



// Create user
CREATE (user:User {
  userId: $userId,
	email: $email,
  username: $username,
  password: $password
})
RETURN user.id

// Create topic
MATCH (user:User { username: $username })
MERGE (user)-[rel:IS]-(author:Author { baseId: $baseId })
	ON CREATE SET author.createdAt = timestamp()
    ON MATCH SET author.lastUsedAt = timestamp()
MERGE (author)-[:WROTE]->(:Dyo { baseId: $baseId, createdAt: timestamp() })
RETURN *

// Create Reply
MATCH (dyo:Dyo { baseId: $baseId })
MERGE (user)-[rel:IS]-(author:Author { baseId: $baseId })
	ON CREATE SET author.createdAt = timestamp()
    ON MATCH SET author.lastUsedAt = timestamp()
MERGE (author)-[wrote:WROTE]->(reply:Reply { createdAt: timestamp() })-[:REPLIES]->(dyo)
RETURN *

// Start dyo
MATCH (baseDyo:Dyo { baseId: $baseId })
MERGE (user)-[rel:IS]-(author:Author { baseId: $baseId })
	ON CREATE SET author.createdAt = timestamp()
    ON MATCH SET author.lastUsedAt = timestamp()
MERGE (author)-[wrote:WROTE]->(dyo:Dyo { createdAt: timestamp(), baseId: $baseId })<-[:PARENT]-(baseDyo)
RETURN *


:params {email: 'john@gmail.com', username: 'johnsnow',  password: '123', baseId: '28', userId: '123', groupId: '44', author: { name: 'Mark', avatar: 'blue'}, dyo: {headline: 'header', body: 'a little of msg', tags: ['hoy','jaz'], privacy: ['*']}, dyoId: '990' }

// Constraints
CREATE CONSTRAINT ON (a:Author) ASSERT a.name IS UNIQUE;
CREATE CONSTRAINT ON (a:Author) ASSERT a.avatar IS UNIQUE;

Activate user, set prop actvated = true. If not activated, then it's loose
