import os
from decouple import config

class Config:
    SECRET_KEY= config('SECRET_KEY','secret')


class DevConfig(Config):
    DEBUG=config('DEBUG', cast=bool)


class TestConfig(Config):
    pass


class ProdConfig(Config):
    DEBUG=config('DEBUG', cast=bool)


config_dict={
    'dev':DevConfig,
    'prod':ProdConfig,
    'test':TestConfig
}