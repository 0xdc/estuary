estuary - a free connection to the open sea
===========================================

Requirements:
* Database server (primarily MySQL, sqlite3 for smaller installations)
* Static file webserver

Install:

```sh
pip install -e git+https://github.com/0xdc/estuary#egg=estuary
```

Development:

```sh
alembic upgrade head
DEBUG=1 python -mestuary
```

Production:

```sh
uvicorn estuary:app
```

Create migrations:

```sh
alembic revision --autogenerate -m "message"
```

Test:

```sh
pip install -e .[test]
coverage run -m pytest
coverage report --include="estuary/*,migrations/*,tests/*" -m
```
