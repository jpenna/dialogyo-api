from dotenv import load_dotenv
from starlette.applications import Starlette
from ariadne.asgi import GraphQL
import os
import debuggers

from middlewares import setup_middlewares
from client_api import schema
from db import GraphDB

load_dotenv()

isDev = os.getenv('ENV') != 'prod'

if isDev:
    if os.getenv('VS_CODE'):
        debuggers.debug_vscode()

app = Starlette(debug=isDev)
setup_middlewares(app)

app.mount('/graphql', GraphQL(schema=schema, debug=isDev))

graphDB = GraphDB()


@app.on_event("startup")
def startup():
    graphDB.connect()


@app.on_event("shutdown")
def shutdown():
    graphDB.disconnect()
