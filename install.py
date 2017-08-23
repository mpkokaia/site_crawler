from pymongo import MongoClient

client = MongoClient()
doc = client.test.html_storage
doc.create_index("url", unique=True)
