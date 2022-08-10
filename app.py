from datetime import timedelta

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from  security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db
import os

app = Flask(__name__)
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)   # config JWT to expire within half an hour

#### this is done because sqlalchemy doesn't support postgres://username:password@hostname.com, rather it supports
### postgresql://username:password@hostname.com
uri = os.environ.get("DATABASE_URL", "sqlite:///data.db")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
### Finished setting up  DATABASE_URL to connect with postgres in heroku

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = "Mayank"
api = Api(app)
jwt = JWT(app, authenticate, identity)  # create /auth resource by default


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)

