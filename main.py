from dotenv import load_dotenv
from starlette.applications import Starlette
from starlette.graphql import GraphQLApp
import os
import graphene
import uvicorn


load_dotenv()


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return "Hello " + name


app = Starlette(debug=os.getenv('DEVELOPMENT'))
app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query)))


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=23400)
