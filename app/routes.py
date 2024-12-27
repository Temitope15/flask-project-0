from flask import Blueprint, request, jsonify  # to create the endpoints
from werkzeug.security import generate_password_hash  # to generate password hash
from functools import wraps
import validators
import re

from app.database import db
from app.models import User, UserSchema

user_bp = Blueprint('users', __name__)

user_schema = UserSchema()  # to serialize or deserialize for a single user object
users_schema = UserSchema(many=True)  # to serialize and desrialize many users

# errror message helper function


def error_response(message, status_code):
    return jsonify({"error": message}), status_code

# password validator helper function


def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long"
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one upperase letter"
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter"
    if not re.search(r'\d', password):
        return "password must contain at least one number"
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "password must contain at least one special character"
    return None


# input validattion helper function
def validate_user_input(data):
    if not data.get('username') or not data.get('email') or not data.get('password') or not data.get('school') or not data.get('department'):
        return "All fields are required"

    if not validators.email(data['email']):
        return "Invalid email format"
    password_error = validate_password(data['password'])
    if password_error:
        return password_error
    if data['password'] != data['confirm_password']:
        return "passwords do not match"
    return None

#helper function to validate token
def validate_bearer_token(request):
    token = request.headers.get('Authorization')
    if token and token.startswith("Bearer "):
        return token.split(" ")[1] == "ey_STEPHENGADE_py024"
    return False

#decorator function
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not validate_bearer_token(request):
            return error_response('Invalid or missing token', 403)
        return f(*args, **kwargs)
    return decorated_function

# to create a new user


@user_bp.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()  # this os to get the input  data from the user
        input_error = validate_user_input(data)

        if input_error:
            return error_response(input_error, 400)

        # if user already exists
        existing_user = User.query.filter(
            (User.username == data['username']) | (User.email == data['email'])
        ).first()
        if existing_user:
            error_response(
                'A user with this email or username already exists', 400)

        # hashing the password using werkzeug.security

        hashed_password = generate_password_hash(data['password'])

        # to  create a new user
        new_user = User(
            # i  did it this way because it is optional to tell us about yourself, check line 21 in models.py
            username=data['username'], email=data['email'], password=hashed_password, about=data.get('about', 'No information provided'),  school=data['school'], department=data['department'], heartrob=data.get('heartrob', 'BISOLA')
        )

        # This will save the user to the database
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user), 201

    except Exception as e:
        db.session.rollback()
        return error_response(
            f'An unexpected error occured: {str(e)}', 500)

# to get all users


@user_bp.route('/users', methods=['GET'])
@token_required
def get_users():
    try:
        users = User.query.all()
        return users_schema.jsonify(users), 200
    except Exception as e:
        return error_response(
            f'An unexpected error occured: {str(e)}', 500)


# to get a specific user
@user_bp.route('/users/<uuid:user_id>', methods=['GET'])
@token_required
def get_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        return user_schema.jsonify(user), 200
    except Exception as e:
        return error_response(
            f'An unexpected error occured:{str(e)}', 500)


# to update the user details
@user_bp.route('/users/<uuid:user_id>', methods=['PATCH'])
def update_user(user_id):
    try:
        user= User.query.get_or_404(user_id)
        data = request.get_json()

        user.school = data.get('school', user.school)
        user.department = data.get('department', user.department)
        user.about = data.get('about', user.bio)
        user.heartrob = data.get('heartrob', user.heartrob)

        db.session.commit()
        return user_schema.jsonify(user), 200
    except Exception as e:
        db.session.rollback()
        return error_response(f'An unexpected error occurred: {str(e)}', 500)


@user_bp.route('/users/<uuid:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        name = User.username
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': f'user {name} ({user_id}) deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return error_response(f'An unexpected error occurred: {str(e)}', 500)
