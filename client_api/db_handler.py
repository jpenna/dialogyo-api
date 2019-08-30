import os
import sys
from graphql.error import GraphQLError


def dispatch_db(callback, *args, **kwargs):
    try:
        return callback(*args, **kwargs)
    except Exception as e:
        if os.getenv('DEVELOPMENT'):
            print(e, file=sys.stderr)
        raise e
