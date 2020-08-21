from starlette.routing import WebSocketRoute  # Route, Mount
from . import views

routes = [
        # Route("/endpoint", endpoint=..., methods=["GET", "POST"], name=...),
        # Mount("/path", routes=[...] name=...),
        WebSocketRoute("/ws", views.echo.Echo),
]
