from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "TicketHub"
    API_V1_PREFIX: str = "/api/v1"

    class Config:
        env_file = ".env"

settings = Settings()
