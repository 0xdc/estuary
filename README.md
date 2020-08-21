estuary - a free connection to the open sea
===========================================

Requirements:
* Database server (primarily MySQL, sqlite3 for smaller installations)
* Static file webserver

Development:

  python -malembic.config upgrade head
  DEBUG=1 python -mestuary

Production:

  uvicorn estuary:app

Create migrations:

  python -malembic.config revision --autogenerate -m "message"

Test:

  coverage run -m pytest
  coverage report
