# Dyalogio API (Python)

## Neo4j

```sh
docker pull neo4j:3.5
```

```sh
docker run \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=/home/juliano/Documents/dyalogio/api/neo4j_/data:/data \
    --volume=/home/juliano/Documents/dyalogio/api/neo4j_/logs:/logs \
    --env=NEO4J_AUTH=none \
    neo4j:3.5
```
