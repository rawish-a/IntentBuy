#This loads values from .env file.
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# path to backend/.env
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"

class Settings(BaseSettings):
    database_url: str = Field(..., alias="DATABASE_URL")
    secret_key:   str = Field(..., alias="SECRET_KEY")

    # --- JWT / Auth ---
    algorithm: str = Field("HS256", alias="ALGORITHM")
    access_token_expire_minutes: int = Field(30, alias="ACCESS_TOKEN_EXPIRE_MINUTES")

    model_config = SettingsConfigDict(
        env_file=str(ENV_PATH),
        case_sensitive=True,
        extra="ignore",
    )

settings = Settings()
