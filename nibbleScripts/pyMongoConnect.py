from pymongo import MongoClient

import datetime

post = {"author": "Mike",
	"text": "My first blog post!",
	"tags": ["mongodb", "python", "pymongo"],
	"date": datetime.datetime.utcnow()}
client = MongoClient()
db = client.NIBBLE
collection = db.restaurant
collection.insert_one(post).inserted_id