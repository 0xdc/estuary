from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles

from . import settings
from .url import routes

if settings.DEBUG:
    from starlette.routing import Mount
    static = StaticFiles(directory="static/dist", html=True)
    routes.append(Mount("/", app=static, name="static"))

app = Starlette(debug=settings.DEBUG, routes=routes)
