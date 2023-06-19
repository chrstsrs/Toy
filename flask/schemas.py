from marshmallow import Schema, fields

class ToySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    quantity = fields.Int(required=True)

class ToyUpdateSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    price = fields.Float()
    quantity = fields.Int()
