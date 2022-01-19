import os
from boto.s3.connection import S3Connection
from pymongo import MongoClient

def mongoConnect():
    uri = S3Connection(os.environ['MONGO_URI'])
    return MongoClient(uri)
