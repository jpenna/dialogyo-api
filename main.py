from dotenv import load_dotenv
from starlette.applications import Starlette
from starlette.graphql import GraphQLApp
from starlette.responses import PlainTextResponse
import os
import debuggers

from middlewares import setupMiddlewares
from client_api import schema
from db import GraphDB

load_dotenv()

isDev = os.getenv('DEVELOPMENT')

if isDev:
    if os.getenv('VS_CODE'):
        debuggers.debug_vscode()

app = Starlette(debug=isDev)
setupMiddlewares(app)

app.add_route('/graphql', GraphQLApp(schema=schema))

graphDB = GraphDB()


@app.on_event("startup")
def startup():
    graphDB.connect()


@app.on_event("shutdown")
def shutdown():
    graphDB.disconnect()


@app.route('/msg/{msg}')
def message(request):
    oi = graphDB.print_greeting(request.path_params['msg'])
    print(oi)
    return PlainTextResponse(oi)
