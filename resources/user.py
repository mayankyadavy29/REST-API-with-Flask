import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="Username of user")
    parser.add_argument("password", type=str, required=True, help="Password of user")

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data["username"]):
            return {"message": "User with that name already exists"}, 400
        UserModel(data["username"], data["password"]).save_to_db()

        return {"message": "User has been registered successfully"}, 201