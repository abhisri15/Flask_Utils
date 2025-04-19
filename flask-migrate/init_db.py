from migrate import db
from migrate import create_app

# This script initializes the database using your Flask app context
app = create_app()

with app.app_context():
    db.create_all()
    print("Database and tables created successfully.")
