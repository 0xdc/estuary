from starlette.endpoints import WebSocketEndpoint
from nejma.ext.starlette.endpoints import WebSocketEndpoint as Nejma


class Echo(WebSocketEndpoint):
    encoding = "text"

    async def on_receive(self, websocket, data):
        await websocket.send_text(data)


class Chat(Nejma):
    encoding = "json"

    async def on_receive(self, websocket, data):
        room_id = data['room_id']
        message = data['message']
        group = f"group_{room_id}"
        self.channel_layer.add(group, self.channel)

        if message.strip():

            payload = {
                    "room_id": room_id,
                    "message": message,
            }
            await self.channel_layer.group_send(group, payload)
