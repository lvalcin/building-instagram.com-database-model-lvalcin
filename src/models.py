from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
# framework for building backend
db = SQLAlchemy()

class User(db.Model):
    # everything needs an id, we always need line 9
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
                # This number in parenthesis above in the character limits, so no more than 120 in this case
    password = db.Column(db.String(20), unique=False, nullable=False)
    # nullable false means it cannot be empty, nullable true means it can be empyt, unique means it has to be unique
    # birthday = db.Column(db.String(12), unique=False, nullable=True) 
    # name = db.Column(db.String(120), unique=False, nullable=True)  
    # post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    posts = db.Relationship("Post",backref ="owner", lazy=True)                                                       


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    date = db.Column(db.String(12), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.Relationship("User")
   

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unread = db.Column(db.Integer, unique=False, nullable=False)
    read = db.Column(db.Integer, unique=False, nullable=False)

class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, unique=False, nullable=False)




    # the code below is connected to the class
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_id": self.user_id,
            # do not serialize the password, its a security breach
        }
