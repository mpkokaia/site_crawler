from pymongo import MongoClient, errors


class Storage:
    def __init__(self):
        client = MongoClient()
        self.doc = client.test97.html_storage

    def insert(self, title="", root="", current_url="", html=""):
        try:
            self.doc.insert_one({"title": title,
                                 "root": root,
                                 "url": current_url,
                                 "html": html})
        except errors.DuplicateKeyError:
            pass

    def get(self, root, limit):
        return self.doc.find({"root": root}, projection={
            "_id": 0,
            "root": 0,
            "html": 0}, limit=limit)
