import os
import secrets
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from sqlalchemy import create_engine, Engine
from typing import ClassVar

load_dotenv(".env", override=True)


class Settings(BaseSettings):
    HOST: str = os.getenv("HOST") or "0.0.0.0"
    PORT: int = os.getenv("PORT") or 5000

    DEBUG: bool = False if not os.getenv("FLASK_DEBUG") else True

    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY") or str(
        secrets.SystemRandom().getrandbits(128))

    DADATA_TOKEN: str = os.getenv("DADATA_TOKEN") or None
    DADATA_SECRET: str = os.getenv("DADATA_SECRET") or None

    ENGINE: ClassVar[Engine] = create_engine(
        'mssql+pyodbc://DESKTOP-8F7T81O\\SQLEXPRESS/ggs_stud?driver=SQL+Server+Native+Client+11.0', echo=True)


settings = Settings()
