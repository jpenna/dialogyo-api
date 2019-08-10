from graphene import (ObjectType, String, List, Field, NonNull)
from graphql_api._data import dyo1, dyo2, reply1, reply2
from graphql_api.types import Dyo, Reply


class Query(ObjectType):
    dyo = Field(Dyo, id=String(required=True))
    dyosList = NonNull(List(NonNull(Dyo)))
    reply = Field(Reply, id=String(required=True))
    repliesList = List(Reply)

    def resolve_dyo(parent, info, id):
        return dyo1 if id == '1' else \
               dyo2 if id == '2' else None

    def resolve_dyosList(parent, info):
        return [dyo1, dyo2]

    def resolve_reply(parent, info, id):
        return reply1 if id == '1' else \
                reply2 if id == '2' else None

    def resolve_repliesList(parent, info, id):
        return [reply1, reply2]
