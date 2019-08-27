from neo4j import GraphDatabase
import os


class GraphDB(object):

    def __init__(self):
        self._uri = 'bolt://127.0.0.1:7687'
        self._user = os.getenv('NEO4J_USER')
        self._password = os.getenv('NEO4J_PASSWORD')

    def connect(self):
        self._driver = GraphDatabase.driver(
            self._uri,
            auth=(self._user, self._password),
        )

    def disconnect(self):
        self._driver.close()

    def print_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.write_transaction(
                self._create_and_return_greeting,
                message
            )
            return greeting

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)",
                        message=message,
                        )
        return result.single()[0]
