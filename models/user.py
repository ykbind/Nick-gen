from extensions import db
from datetime import datetime

class User:
    collection = "users"

    @staticmethod
    def create(name, habit_score, habit_tag, intelligence_score, intelligence_level, nickname):
        user_doc = {
            "name": name,
            "habit_score": habit_score,
            "habit_tag": habit_tag,
            "intelligence_score": intelligence_score,
            "intelligence_level": intelligence_level,
            "nickname": nickname,
            "avatar_path": "",
            "skills": [],
            "created_at": datetime.utcnow()
        }
        result = db.db[User.collection].insert_one(user_doc)
        user_doc["_id"] = result.inserted_id
        return user_doc

    @staticmethod
    def get_by_id(user_id):
        from bson.objectid import ObjectId
        return db.db[User.collection].find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def get_all():
        return list(db.db[User.collection].find().sort("created_at", -1))

    @staticmethod
    def update_avatar(user_id, avatar_path):
        from bson.objectid import ObjectId
        db.db[User.collection].update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"avatar_path": avatar_path}}
        )

    @staticmethod
    def add_skill(user_id, skill_data):
        from bson.objectid import ObjectId
        db.db[User.collection].update_one(
            {"_id": ObjectId(user_id)},
            {"$push": {"skills": skill_data}}
        )
