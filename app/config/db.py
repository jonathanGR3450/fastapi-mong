from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")
mongo_uri = config["MONGO_URI"]

conn = MongoClient(mongo_uri)
