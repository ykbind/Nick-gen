from extensions import db

class Skill(db.Model):
    __tablename__ = 'skills'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    language = db.Column(db.String(100), nullable=False)
    expertise_level = db.Column(db.Integer, nullable=False) # 1-5 scale
    badge = db.Column(db.String(50)) # Beginner, Intermediate, Advanced
    
    def __repr__(self):
        return f'<Skill {self.language} level {self.expertise_level}>'
