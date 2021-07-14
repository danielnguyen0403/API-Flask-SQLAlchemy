import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity

from db import db

from resources.user import UserRegister
from resources.item import ItemList, Item
from resources.store import Store, StoreList

app = Flask(__name__)

database_url = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://",1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'daniel'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>') 
api.add_resource(Store, '/store/<string:name>')

api.add_resource(UserRegister,'/register')

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000)