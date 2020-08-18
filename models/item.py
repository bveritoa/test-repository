#import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))  #stores is the db and id is the column
    store = db.relationship('StoreModel')



    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name':self.name,'price':self.price}

    @classmethod  # because return an object of type IdemModel
    def find_by_name(cls,name):

        # SQLAlchemy
        #return ItemModel.query.filter_by(name=name).filter_by(id=1)   #what first filter do: SELECT * FROM items WHERE name=name
        #but better look

        #return ItemModel.query.filter_by(name=name).first() #SELECT * FROM items WHERE name=name LIMIT 1 (limit one mean that will take first item
        #this return a ItemModel object that has a self.name and a self.price

        #because is a class method instead of ItemModel can use cls
        return cls.query.filter_by(
            name=name).first()  # SELECT * FROM items WHERE name=name LIMIT 1 (limit one mean that will take first item

        # #sql lite
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM items WHERE name=?"  # from all get the one with name
        # result = cursor.execute(query, (name,))  # (name,) totell pythonis a tuple!
        # row = result.fetchone()
        # connection.close()
        #
        # if row:
        #     #return cls(row[0], row[1]) # or more elegant use argument unpacking
        #     return cls(*row) #it pass each of the arguments for each of the elements

    def save_to_db(self):  # this insert and also update(cause of id)
        db.session.add(self)
        db.session.commit()

    # #sqllite
    #def insert(self):

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO items VALUES (?,?)"
        # cursor.execute(query, (self.name, self.price))
        #
        # connection.commit()
        # connection.close()

    # def update(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #
    #     query = "UPDATE items SET price=? WHERE name=?"
    #     cursor.execute(query, (self.price, self.name))
    #
    #     connection.commit()
    #     connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()