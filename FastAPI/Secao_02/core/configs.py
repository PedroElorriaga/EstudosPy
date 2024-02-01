from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


# SÃO AS CONFIGURAÇÕES GERAIS USADAS NA APLICAÇÃO
class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = ''
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True  # é rigido com letras maiusculas ou minusculas


settings = Settings()
