from app import app
from db import db

@app.before_request
def before_request():
    db.create_all()

db.init_app(app)