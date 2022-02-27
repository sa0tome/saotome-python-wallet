from flask_marshmallow import Marshmallow
from marshmallow import fields, EXCLUDE
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import Product, Customer, Order

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        unknown = EXCLUDE 

class CustomerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        unknown = EXCLUDE 

class OrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        customer = fields.Nested(CustomerSchema)
        products = fields.List(fields.Nested(ProductSchema))
        unknown = EXCLUDE 
