from flask import Blueprint, request
from marshmallow import exceptions
from .serializers import OrderSchema, CustomerSchema, ProductSchema

bp_cashback = Blueprint('cashback', __name__)

@bp_cashback.route('/api/cashback', methods=['POST'])
def cashback():
    os = OrderSchema()
    try:
        order = os.load(request.json)
    except exceptions.ValidationError as e:
        message = e.normalized_messages()
        return message, 400
    return order, 201
