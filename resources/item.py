from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=float, required=True, help="Price of item")
    parser.add_argument("store_id", type=int, required=True, help="Store id where it will be stored")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_item_by_name(name)
        if item:
            return item.json()
        return {"message": f"Item {name} does not exist"}, 404

    def post(self, name):
        if ItemModel.find_item_by_name(name):
            return {"message": f"An item with name {name} already exists."}, 400

        req_body = self.parser.parse_args()
        item = ItemModel(name, req_body["price"], req_body["store_id"])
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred while inserting item in database"}, 500
        return item.json(), 201

    def delete(self, name):
        try:
            item = ItemModel.find_item_by_name(name)
            if item:
                item.delete_from_db()
        except:
            return {"message": "An error occurred while inserting item in database"}, 500
        return {"message": "Item deleted successfully"}

    def put(self, name):
        data = self.parser.parse_args()
        item = ItemModel.find_item_by_name(name)
        if item:
            item.price = data["price"]
            item.store_id = data["store_id"]
        else:
            item = ItemModel(name, data["price"], data["store_id"])
        item.save_to_db()
        return item.json()

class ItemList(Resource):
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}