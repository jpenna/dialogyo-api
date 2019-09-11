import os
from ariadne import make_executable_schema, load_schema_from_path

from client_api.mutations import mutation
from client_api.queries import query

type_defs = load_schema_from_path(os.path.abspath("client_api/schema.graphql"))

schema = make_executable_schema(
    type_defs,
    [query, mutation]
)
