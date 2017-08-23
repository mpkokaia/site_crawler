from pymongo import MongoClient

client = MongoClient()
doc = client.test97.html_storage
doc.create_index("url", unique=True)
