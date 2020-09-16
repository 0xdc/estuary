import os
from starlette.config import Config
from starlette.datastructures import Secret, URL

config = Config(".env")

DEBUG = config('DEBUG', cast=bool, default=False)
SECRET_KEY = config('SECRET_KEY', cast=Secret, default=os.urandom(32))
DATABASE_URL = config('DATABASE_URL', cast=URL, default="sqlite:///db.sqlite")
