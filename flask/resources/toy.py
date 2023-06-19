from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ToyModel
from schemas import ToySchema, ToyUpdateSchema

blp = Blueprint("toys","toys",description="Operation on soft toys")

@blp.route("/catalog/<string:name>")
class Toy(MethodView):
    @blp.response(200, ToySchema)
    @blp.alt_response(404, description="Toy not found.")
    def get(self, name):
        toy = ToyModel.query.filter_by(name=name).first_or_404()
        return toy

@blp.route("/catalog/<int:id>")
class ToyDel(MethodView):
    @blp.response(204)
    def delete(self, id):
        try:
            toy = ToyModel.query.get(id)
            db.session.delete(toy)
            db.session.commit()
        except:
            pass

    @blp.arguments(ToyUpdateSchema)
    @blp.response(200, ToySchema)
    @blp.alt_response(422, description="This name is in use. Cannot update")
    @blp.alt_response(404, description="Can not update the toy. Toy not found.")
    def put(self, toy_data, id):
        toy = ToyModel.query.get_or_404(id)
        toy.name = toy_data["name"]
        toy.description = toy_data["description"]
        toy.price = toy_data["price"]
        toy.quantity = toy_data["quantity"]
        try:
            db.session.add(toy)
            db.session.commit()
        except:
            abort(422)
        return toy

@blp.route("/catalog")
class ToyList(MethodView):
    @blp.response(200, ToySchema(many=True))
    def get(self):
        return ToyModel.query.all()

    @blp.arguments(ToySchema)
    @blp.response(201, ToySchema)
    def post(self, toy_data):
        toy = ToyModel(**toy_data)
        try:
            db.session.add(toy)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the toy.")

        return toy
