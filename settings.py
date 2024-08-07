import os
import secrets
from dotenv import load_dotenv
load_dotenv()

HOST = os.getenv("HOST") or "0.0.0.0"
PORT = os.getenv("PORT") or 5000
DEBUG = False if not os.getenv("FLASK_DEBUG") else True
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY") or str(
    secrets.SystemRandom().getrandbits(128))
DADATA_TOKEN = os.getenv("DADATA_TOKEN") or None
DADATA_SECRET = os.getenv("DADATA_SECRET") or None
