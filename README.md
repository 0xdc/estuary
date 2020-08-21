estuary - a free connection to the open sea
===========================================

Requirements:
* Database server (primarily MySQL, sqlite3 for smaller installations)
* Static file webserver

Install:

  pip install -e git+https://github.com/0xdc/estuary#egg=estuary

Development:

  alembic upgrade head  
  DEBUG=1 python -mestuary

Production:

  uvicorn estuary:app

Create migrations:

  alembic revision --autogenerate -m "message"

Test:

  pip install -e .[test]  
  coverage run -m pytest  
  coverage report --include="estuary/*,migrations/*,tests/*" -m
