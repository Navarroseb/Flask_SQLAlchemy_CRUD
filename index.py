from app import app
from utils.db import db

@app.before_request
def create_database():
     db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
