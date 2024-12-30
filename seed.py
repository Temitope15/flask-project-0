from app import create_app
from app.database import db
from app.models import User
from werkzeug.security import generate_password_hash
import uuid

app = create_app()

with app.app_context():
    # Create a new user with the updated model
    new_user = User(
        id=uuid.uuid4(),
        username='testuser',
        email='testuser@example.com',
        password=generate_password_hash('password123'),
        about='This is a test user'
    )

    # Add the user to the database
    db.session.add(new_user)
    db.session.commit()
    print("Database seeded successfully!")
