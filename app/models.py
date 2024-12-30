# import  db, ma for database and schema
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database import db, ma
# to get the time stamp when the user creates account
from datetime import datetime, timezone

# to create the database table


class User(db.Model):
    __tablename__ = 'users'  # table name set to users

    # columns of the table
    # i.e it is the primary key that wil be used to keep tracck the number of users in my database
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # the username table, is a string that can not be more than 100 characters and it cannot be empty
    username = db.Column(db.String(100), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    # this will automatially save the time the  user creates an account, i am not using datatimr.utcnow because i saw it was deprecated, so instead i am using datetime.now(timezone.utc)
    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc))
    password = db.Column(db.String(255), nullable=False)

    # its optional to tell me about you
    about = db.Column(db.String, nullable=True)

    # #the school you attend
    # school = db.Column(db.String, nullable=False)

    # department = db.Column(db.String, nullable=False)
    # heartrob = db.Column(db.String, default='BISOLA', nullable=True)


def __repr__(self):
    return f'<User {self.username}>'  # return the username of the user

# to  convert a User object to/from JSOn


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    # This ensures the password is only used when receiving data, not when sending it...literally not to e xpose the password during serialization
    password = ma.auto_field(load_only=True)
