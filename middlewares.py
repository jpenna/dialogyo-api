from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.cors import CORSMiddleware
# from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.gzip import GZipMiddleware
import os

isDev = os.getenv('DEVELOPMENT')
allowedHosts = ['dyalogio.com', 'dialogyo.com', 'dyalogyo.com']


def setupMiddlewares(app):
    if not isDev:
        app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=allowedHosts,
        )
        app.add_middleware(
            HTTPSRedirectMiddleware
        )
        app.add_middleware(
            CORSMiddleware,
            allow_origin=[f'https://{host}' for host in allowedHosts],
            allow_methods=['*'],
        )
        # app.add_middleware(
        #     SessionMiddleware,
        #     secret_key=os.getenv('SESSION_SECRET_KEY'),
        #     same_site='lax',
        #     https_only=not isDev,
        # )
        app.add_middleware(
            GZipMiddleware,
            minimum_size=1000,
        )
