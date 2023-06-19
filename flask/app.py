# import os

from flask import Flask # , request
from flask_smorest import Api #, abort
# from resources.toy import blp as ToyBlueprint
# from flask_migrate import Migrate
from db import db

import models

from resources.toy import blp as ToyBlueprint


# blueprints

def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ToyBlueprint)

    return app
# create_app()
# stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]}]
# catalog = [{"name":"smilyball", "description":"A smily tenis ball", "price":12,"quantity":7}]
#
#
# # @app.get("/store")
# # def get_stores():
# #     return {"stores": stores}
#
# @app.get("/catalog")
# def get_all_toys():
#     return {"catalog": list(toy.values())}
#
# # @app.post("/store")
# # def create_store():
# #     request_data = request.get_json()
# #     new_store = {"name": request_data["name"], "items": []}
# #     stores.append(new_store)
# #     return new_store, 201
#
# @app.post("/catalog")
# def create_item():
#     request_data = request.get_json()
#     new_toy = { "name": request_data["name"],
#                 "description":request_data["description"],
#                 "price": request_data["price"],
#                 "quantity": request_data["quantity"]}
#     toys.append(new_toy)
#     return new_toy, 201
#
# # @app.post("/store/<string:name>/item")
# # def create_item(name):
# #     request_data = request.get_json()
# #     for store in stores:
# #         if store["name"] == name:
# #             new_item = {"name": request_data["name"], "price": request_data["price"]}
# #             store["items"].append(new_item)
# #             return new_item, 201
# #     return abort(404, "message"="Store not found")
#
# @app.get("/catalog/<string:name>")
# def get_toy(name):
#     for toy in toys:
#         if toy["name"] == name:
#             return {"toys": toy["toys"]}
#     return {"message": "Toy not found"}, 404
#
# # @app.get("/store/<string:name>")
# # def get_store(name):
# #     for store in stores:
# #         if store["name"] == name:
# #             return store
# #     return abort(404, "message"="Store not found")
#
#
# # @app.get("/store/<string:name>/item")
# # def get_item_in_store(name):
# #     for store in stores:
# #         if store["name"] == name:
# #             return {"items": store["items"]}
# #     return {"message": "Store not found"}, 404
