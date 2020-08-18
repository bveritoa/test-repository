import sqlite3
from db import db

class UserModel(db.Model):
    __tabelname__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80))  #limit 80 chars
    password = db.Column(db.String(80))
# this properies(down) must match the column from db(up) or will not give an error but it will be ignored!!!

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

        # connection = sqlite3.connect('data.db')  # init connectiom
        # cursor = connection.cursor()  # init cursor
        #
        # query = "SELECT * FROM users WHERE username=?"
        # result = cursor.execute(query, (username,))  # couse need to be as a tuple
        # row = result.fetchone()  # get first row of result set
        # # if row is not None:   #no rows
        # # or
        # if row:
        #     user = cls(row[0], row[1], row[2])  # create an obj with that data id username and password.they have to match the paramin init method
        # else:
        #     user = None
        #
        # connection.close()
        # return user

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

        # connection = sqlite3.connect('data.db')  # init connectiom
        # cursor = connection.cursor()  # init cursor
        #
        # query = "SELECT * FROM users WHERE id=?"
        # result = cursor.execute(query, (_id,))  # couse need to be as a tuple
        # row = result.fetchone()  # get first row of result set
        # # if row is not None:   #no rows
        # # or
        # if row:
        #     user = cls(row[0], row[1], row[2])  # create an obj with that data id username and password.they have to match the paramin init method
        # else:
        #     user = None
        #
        # connection.close()
        # return user