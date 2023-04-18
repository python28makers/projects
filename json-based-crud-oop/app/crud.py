import json
from json.decoder import JSONDecodeError


class CRUD:
    def write_to_db(self, data):
        with open('db.json', 'w') as db:
            json.dump(data, db, indent=4, ensure_ascii=False)

    def read_db(self):
        try:
            with open('db.json', 'r') as db:
                    return json.load(db)
        except JSONDecodeError:
            return []
        
    def get_object(self, uid):
        with open('db.json', 'r') as db:
            for user in json.load(db):
                if uid == user['uid']:
                    return user
            return None

