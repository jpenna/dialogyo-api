import os
from ariadne import snake_case_fallback_resolvers, make_executable_schema
from ariadne import load_schema_from_path

from client_api.mutations import mutation
# import client_api.queries as query

type_defs = load_schema_from_path(os.path.abspath("client_api/schema.graphql"))

schema = make_executable_schema(
    type_defs,
    [mutation, snake_case_fallback_resolvers]
)
