
from pymongo import MongoClient
from datetime import datetime, timedelta
import os
import sys
from config.constants import app_config
from dotenv import load_dotenv
load_dotenv()


app_configuration = app_config.get(os.getenv("FLASK_ENV"))


def connect_mongo(tenant):
    print("MONGO_URI", app_configuration.MONGO_URI)
    client = MongoClient(app_configuration.MONGO_URI)
    db = client[f'{app_configuration.DB_NAME}_{tenant.lower()}']
    return db
