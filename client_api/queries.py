import db.dyo as dyoDB
from ariadne import QueryType
# from app_errors import ApiError

query = QueryType()


@query.field('dyo')
def resolve_query_dyo(_, info, id: str):
    return dyoDB.get_dyo_by_id(dyoId=id)
