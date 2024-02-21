from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict

app_configs = {"title": "My Cool API"}


class Settings(BaseSettings):

    MODE: Literal["TEST", "DEV", "PROD"]

    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str

    TEST_DB_NAME: str
    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_USER: str
    TEST_DB_PASS: str

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str


    REDIS_HOST: str
    REDIS_PORT: int
    
    DOCS: str

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @property
    def test_database_url(self):
        return f"postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}"
    
    @property
    def get_config(self):
        HOW_DOCS_ENVIRONMENT = ("local", "staging")
        if self.DOCS not in HOW_DOCS_ENVIRONMENT:
            app_configs["openapi_url"] = None
        
        return app_configs

    
settings = Settings()