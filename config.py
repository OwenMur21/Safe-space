import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') 



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ozzy:ozzie21@localhost/haven'
    DEBUG = True

config_options ={
"production":ProdConfig,
"development":DevConfig
}

