def test_echo(client):
    with client.websocket_connect(client.app.url_path_for("echo")) as ws:
        ws.send_text("hello world")
        data = ws.receive_text()
        assert data == "hello world"
