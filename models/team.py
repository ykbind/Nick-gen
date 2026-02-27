from extensions import db
from datetime import datetime

class Team:
    collection = "teams"

    @staticmethod
    def create(team_name):
        team_doc = {
            "team_name": team_name,
            "created_at": datetime.utcnow()
        }
        db.db[Team.collection].insert_one(team_doc)
        return team_doc

    @staticmethod
    def get_all():
        return list(db.db[Team.collection].find())
