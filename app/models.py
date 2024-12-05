#import  db, ma for database and schema 
from app.database import db, ma
#to get the time stamp when the user creates account
from datetime import datetime, timezone

#to create the database table
class User(db.Model):
    __tablename__ = 'users' #table name set to users

    # columns of the table
    id = db.Column(db.Integer, primary_key=True) #i.e it is the primary key that wil be used to keep tracck the number of users in my database

    # the username table, is a string that can not be more than 100 characters and it cannot be empty
    username = db.Column(db.String(100), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc)) #this will automatially save the time the  user creates an account, i am not using datatimr.utcnow because i saw it was deprecated, so instead i am using datetime.now(timezone.utc)
    password = db.Column(db.String(255), nullable=False)

    about = db.Column(db.String, nullable=True) #its optional to tell me about you

def __repr__(self):
    return f'<User {self.username}>' #return the username of the user

# to  convert a User object to/from JSOn
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    password = ma.auto_field(load_only=True) # This ensures the password is only used when receiving data, not when sending it...literally not to e xpose the password during serialization