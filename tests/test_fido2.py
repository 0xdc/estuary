def test_registration_begin_get(client):
    response = client.get(client.app.url_path_for("registration_begin"))

    j = response.json()

    assert 'name' in j
    assert 'id' in j


def test_registration_begin_post(client):
    from fido2 import cbor

    response = client.post(client.app.url_path_for("registration_begin"))

    c = cbor.decode(response.content)

    assert 'id' in c
    assert 'name' in c
