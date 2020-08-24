from starlette.endpoints import HTTPEndpoint
from starlette.responses import Response, JSONResponse
import secrets
from fido2.utils import bytes2int
from fido2 import cbor


class RegistrationBegin(HTTPEndpoint):
    async def post(self, request):
        user_cred = {
            "id": secrets.token_bytes(32),
            "name": secrets.token_urlsafe(16)
        }
        cresp = cbor.encode(user_cred)
        response = Response(cresp, media_type="application/octet-stream")
        await response(self.scope, self.receive, self.send)

    def get(self, request):
        user_cred = {
            "id": bytes2int(secrets.token_bytes(32)),
            "name": secrets.token_urlsafe(16)
        }
        return JSONResponse(user_cred)
