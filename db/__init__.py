from neo4j import GraphDatabase
import os


class GraphDB(object):

    _driver = None
    _uri = 'bolt://127.0.0.1:7687'
    _user = os.getenv('NEO4J_USER')
    _password = os.getenv('NEO4J_PASSWORD')

    @staticmethod
    def connect():
        if not GraphDB._driver:
            GraphDB._driver = GraphDatabase.driver(
                GraphDB._uri,
                auth=(GraphDB._user, GraphDB._password),
            )

    def disconnect(self):
        GraphDB._driver.close()
