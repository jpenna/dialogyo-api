import os
from ariadne import make_executable_schema
from ariadne import load_schema_from_path

from client_api.mutations import mutation

type_defs = load_schema_from_path(os.path.abspath("client_api/schema.graphql"))

schema = make_executable_schema(
    type_defs,
    [mutation]
)
