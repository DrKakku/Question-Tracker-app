from backend import db
from datetime import datetime,timezone

class QuestionsTest(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200),unique=True)
    dateJoined = db.Column(db.Date, default=datetime.now())

    def __repr__(self):
        return f"<User: {self.name}, Email: {self.email}, id:{self.id}>"
    

