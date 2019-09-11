import functools
import os
import threading
from neo4j import GraphDatabase, ServiceUnavailable
from time import sleep


class GraphDB(object):

    _driver = None
    _uri = 'bolt://127.0.0.1:7687'
    _user = os.getenv('NEO4J_USER', '')
    _password = os.getenv('NEO4J_PASSWORD', '')

    @staticmethod
    def connect():
        if GraphDB._driver:
            return
        threading.Thread(target=GraphDB.do_connect, daemon=True).start()

    @classmethod
    def do_connect(cls):
        try:
            # Single threads
            print('Connecting to Neo4j...')
            cls._driver = GraphDatabase.driver(
                cls._uri,
                auth=(cls._user, cls._password),
            )
            print('Neo4j connected!')
        except (ServiceUnavailable, OSError):
            sleep(5)
            cls.do_connect()

    @staticmethod
    def disconnect():
        GraphDB._driver.close()

    @staticmethod
    def tx_write(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with GraphDB._driver.session() as session:
                return session.write_transaction(func, *args, **kwargs)
        return wrapper
