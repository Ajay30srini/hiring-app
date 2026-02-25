from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_TITLE: str = "Hiring App"
    DATABASE_URL: str
    DEBUG: bool = False

settings = Settings()