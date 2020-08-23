from starlette.routing import WebSocketRoute  # Route, Mount
from . import views

routes = [
        # Route("/endpoint", endpoint=..., methods=["GET", "POST"], name=...),
        # Mount("/path", routes=[...] name=...),
        WebSocketRoute("/echo", views.echo.Echo, name="echo"),
        WebSocketRoute("/chat", views.echo.Chat, name="chat"),
]
