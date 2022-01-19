import os

from pymongo import MongoClient

def mongoConnect():
    uri = os.environ.get('MONGO_URI', None)
    return MongoClient(uri)
