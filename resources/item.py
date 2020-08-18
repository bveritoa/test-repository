#import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be left blank'
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='Every item need a store id'
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        else:
            return {'message':'Item not found'}, 404

    def post(self,name):

        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' aldeady exists".format(name)},400 #400 means something was wrong with the request

        #data = request.get_json()
        data = Item.parser.parse_args()

        # item = ItemModel(name, data['price'], data['store_id']) #or more easy write
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "A error occured inserting the item"},500 # 500 means internal server error


        return item.json(), 201  # to know that worked

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return{'message': 'Item deleted'}


        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "DELETE FROM items WHERE name=?"  # from all get the one with name
        # cursor.execute(query, (name,))  # (name,) to tell python is a tuple!
        #
        # connection.commit()
        # connection.close()
        #
        # return {'message': 'Item deleted'}

    def put(self,name):
        data = Item.parser.parse_args()
        #item = next(filter(lambda x: x['name'] == name,items), None)
        item = ItemModel.find_by_name(name)
        #updated_item = ItemModel(name, data['price'])

        if item is None:

            #item = ItemModel(name, data['price'], data['store_id']) #or more easy write
            item = ItemModel(name, **data)
            # try:
            #     updated_item.insert()
            # except:
            #     return {'message':'An error occurred inserting the item'},500
        else:
            item.price = data['price']
            # try:
            #     updated_item.insert()
            # except:
            #     return {'message': 'An error occurred inserting the item'}, 500
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        #return {'items': [item.json() for item in ItemModel.query.all()]}
        return {'items': [x.json() for x in ItemModel.query.all()]}
        #or using lambda
        #return {'items': list(map(lambda x: x.jason(), ItemModel.query.all()))}


        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # items = []
        # for row in result:
        #     items.append({'name':row[0],'price':row[1]})
        # connection.close()

