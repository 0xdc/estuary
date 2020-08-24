from starlette.routing import Route
from . import views

routes = [
        # Route("/endpoint", endpoint=..., methods=["GET", "POST"], name=...),
        # Mount("/path", routes=[...] name=...),
        # WebSocketRoute("/socket", endpoint=..., name=...),
        Route("/api/registration/begin", views.fido2.RegistrationBegin, name="registration_begin")
]
