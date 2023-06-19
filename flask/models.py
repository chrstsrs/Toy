from db import db

class ToyModel(db.Model):
    __tablename__ = "toys"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float(precision=2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
