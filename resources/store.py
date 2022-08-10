from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_item_by_name(name)
        if store:
           return store.json()
        return {"message": f"Store {name} does not exist"}, 404

    def post(self, name):
        if StoreModel.find_item_by_name(name):
            return {"message": f"Store {name} already exists"}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred while saving store in database"}, 500
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_item_by_name(name)
        if store:
            try:
                store.delete_from_db()
            except:
                return {"message": "An error occurred while deleting store from database"}, 500
        return {"message": "Store deleted successfully"}


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}