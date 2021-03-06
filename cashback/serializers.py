from flask_marshmallow import Marshmallow
from marshmallow import fields, validate, EXCLUDE
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


from .models import Product, Customer, Order
from .validators import validate_type, validate_cpf, validate_value


ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class ProductSchema(SQLAlchemyAutoSchema):
    type = fields.Str(validate=validate_type)
    value = fields.Decimal(validate=validate_value)
    class Meta:
        model = Product
        unknown = EXCLUDE 

class CustomerSchema(SQLAlchemyAutoSchema):
    document = fields.Str(validate=validate.And(validate.Length(equal=11), validate_cpf))
    class Meta:
        model = Customer
        unknown = EXCLUDE 

class OrderSchema(SQLAlchemyAutoSchema):
    customer = fields.Nested(CustomerSchema)
    products = fields.List(fields.Nested(ProductSchema))
    total = fields.Decimal(validate=validate_value)
    class Meta:
        model = Order
        unknown = EXCLUDE 
