from pymongo import MongoClient


client = MongoClient('mongodb+srv://root:root@cluster.lf1hr.mongodb.net/?retryWrites=true&w=majority')

db = client.crud