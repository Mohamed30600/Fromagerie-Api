from pydantic import BaseSettings

#Template pydantic pour gérer le fichier de configuration .env
class Settings(BaseSettings):
    provider : str
    host : str
    user : str
    passwd : str
    db : str
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

