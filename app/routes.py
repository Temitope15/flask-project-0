from flask import Blueprint, request, jsonify #
from app.database import db
from app.models import User, UserSchema

user_bp = Blueprint('users', __name__)

user_schema = UserSchema() #to serialize or deserialize for a single user object
users_schema = UserSchema(many=True) #to serialize and desrialize many users

#to create a new user
@user_bp.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json() # this os to get the input  data from the user
        if not data.get('username') or not data.get('email'):
            return jsonify({"Error": "Username and email are required"}), 400
        elif not data.get('password'):
            return jsonify({'Error': "Password is required" }), 400
            
        #if user already exists
        existing_user = User.query.filter(
            (User.username == data['username']) | (User.email == data['email'])
        ).first()
        if existing_user:
            return jsonify({"error":" You already have an account"}), 400
        
        new_user = User(
            username=data['username'], email=data['email'], password=data['password'], about=data['about'])
        
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500