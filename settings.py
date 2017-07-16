"""
Simple configuration file. It also checks if you have any local settings defined, in which case it overrides the default values
"""
import os

SQLALCHEMY_DATABASE_URI = 'sqlite://'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_POOL_RECYCLE = 299

SECRET_KEY = os.urandom(24)