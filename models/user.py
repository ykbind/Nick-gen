from extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    habit_score = db.Column(db.Integer, default=0)
    intelligence_score = db.Column(db.Integer, default=0)
    intelligence_level = db.Column(db.String(50)) # Beginner, Intermediate, Pro
    nickname = db.Column(db.String(150))
    avatar_path = db.Column(db.String(255))
    habit_tag = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    skills = db.relationship('Skill', backref='user', lazy=True)
    
    def __repr__(self):
        return f'<User {self.name}>'
