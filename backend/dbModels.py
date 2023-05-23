from datetime import datetime

from backend import db


class QuestionsTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    dateJoined = db.Column(db.Date, default=datetime.now())

    def __repr__(self):
        return f"<User: {self.name}, Email: {self.email}, id:{self.id}>"
    


class Questions(db.Model):
    Id = db.Column(db.Integer,primary_key=True)
    QuestionName =    db.Column(db.String(500),nullable=False)
    QuestionURL =     db.Column(db.String(500)) 
    QuestionStatus =  db.Column(db.Boolean,default=False)
    StartDate =       db.Column(db.Date,default=datetime.now()) 
    StartTime =       db.Column(db.Time,default=datetime.now().time())
    EndDate =         db.Column(db.Date) 
    EndTime =         db.Column(db.Time) 
    TotalTimeM =      db.Column(db.Integer) 
    TotalTimeS =      db.Column(db.BigInteger) 
    Description =     db.relationship("Description",backref="questions")
    Solution =        db.relationship("Solutions",backref="questions")
    def __repr__(self):
        return f"<Id: {self.Id}, QuestionName: {self.QuestionName}, Description:{self.Description}, StartTime:{self.StartTime}>"
    
    def toDict(self):
        dic = {
            "Id":                    self.Id,
            "QuestionName":          self.QuestionName ,
            "QuestionURL":           self.QuestionURL ,
            "QuestionStatus":        self.QuestionStatus ,
            "StartDate":             self.StartDate.isoformat() if self.StartDate else None,
            "StartTime":             self.StartTime.isoformat() if self.StartTime else None ,
            "EndDate":               self.EndDate.isoformat() if self.EndDate else None ,
            "EndTime":               self.EndTime.isoformat()  if self.EndTime else None,
            "TotalTimeM":            self.TotalTimeM ,
            "TotalTimeS":            self.TotalTimeS ,
            "Description":           [i.toDict() for i in  self.Description] ,
            "Solution":              [i.toDict() for i in self.Solution] ,
            "type":                  "Questions",
        }
        return dic



class Description (db.Model):
    Id = db.Column(db.Integer, primary_key = True)
    Description = db.Column(db.Text, nullable = False) #change the type later to LargeBinary
    QuestionId = db.Column(db.Integer,db.ForeignKey('questions.Id'))	

    def __repr__(self):
        return f"{self.Id}, {self.Description}"
    
    def toDict(self):
        dic = {
                "Id":                      self.Id  ,
                "Description":             self.Description  ,
                "QuestionId ":             self.QuestionId   ,
                "type":                    "Description",

        }
        return dic



class Solutions (db.Model):
    Id = db.Column(db.Integer, primary_key = True)
    Solution = db.Column(db.Text, nullable = False)
    QuestionId = db.Column(db.Integer,db.ForeignKey('questions.Id'))	
    
    def __repr__(self):
        return f"{self.Id}, {self.Solution}"
	
    def toDict(self):
        dic = {
                "Id":                      self.Id  ,
                "Solution":                self.Solution  ,
                "QuestionId ":             self.QuestionId   ,
                "type":                    "Solution",
        }
        return dic
