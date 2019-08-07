from dotenv import load_dotenv
from starlette.applications import Starlette
from starlette.graphql import GraphQLApp
import os
import uvicorn

from graphql_api.schema import schema


load_dotenv()


app = Starlette(debug=os.getenv('DEVELOPMENT'))
app.add_route('/graphql', GraphQLApp(schema=schema))


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=23400)
