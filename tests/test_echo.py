def test_echo(client):
    with client.websocket_connect(client.app.url_path_for("echo")) as ws:
        ws.send_text("hello world")
        data = ws.receive_text()
        assert data == "hello world"

def test_chat(client):
    with client.websocket_connect(client.app.url_path_for("chat")) as ws:
        ws.send_json({
            "room_id": "chat",
            "message": "test of chat"
        })
        data = ws.receive_json()
        assert data['room_id'] == "chat"
        assert data['message'] == "test of chat"
