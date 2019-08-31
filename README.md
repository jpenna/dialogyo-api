# Dyalogio API (Python)

## Neo4j

```sh
docker pull neo4j:3.5
```

```sh
mkdir $PWD/_neo4j/plugins
curl https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download/3.4.0.7/apoc-3.4.0.7-all.jar \
    -o $PWD/_neo4j/plugins/apoc-3.4.0.7-all.jar

docker run \
    --name dyo-neo4j \
    -p 7474:7474 -p 7687:7687 \
    -v $PWD/_neo4j/data:/data \
    -v $PWD/_neo4j/logs:/logs \
    -v $PWD/_neo4j/plugins:/plugins \
    -e NEO4J_dbms_security_procedures_unrestricted=apoc.\\\* \
    -e NEO4J_apoc_export_file_enabled=true \
    -e NEO4J_apoc_import_file_enabled=true \
    -e NEO4J_apoc_import_file_use__neo4j__config=true \
    -e NEO4J_AUTH=none \
    neo4j:3.5.8
```

 Install APOC: https://neo4j-contrib.github.io/neo4j-apoc-procedures/3.4/installation/

## Errors

1 - Invalid Value
99 - Unknown Error
