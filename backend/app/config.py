#This loads values from .env file.
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    database_url: str
    secret_key: str

    model_config = SettingsConfigDict(env_file=str(Path(__file__).resolve().parent.parent / ".env"))
    #Loads values from the .env file into the settings instance.

settings = Settings()