from graphene.test import Client
from client_api.schema import schema
from snapshottest import TestCase


class TestClass(TestCase):
    def test_dyo_no_id(self):
        '''Should return error'''
        client = Client(schema)
        self.assertMatchSnapshot(client.execute('''{ dyo { name } }'''))
