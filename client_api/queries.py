from ariadne import QueryType, ObjectType
from client_api._data import dyo1, dyo2, reply1, reply2

dyo = QueryType()


@dyo.field('dyo')
def resolve_dyo(_, info, dyo, author, parentId, ):
    return dyo1 if id == '1' else \
            dyo2 if id == '2' else None

# def resolve_dyosList(parent, info):
#     return [dyo1, dyo2]

# def resolve_reply(parent, info, id):
#     return reply1 if id == '1' else \
#             reply2 if id == '2' else None

# def resolve_repliesList(parent, info, id):
#     return [reply1, reply2]
