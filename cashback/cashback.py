from flask import Blueprint, request
from marshmallow import exceptions
from .serializers import OrderSchema, CustomerSchema, ProductSchema
from .utils import calculate_cashback
import requests

EXTERNAL_API_URL = 'https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback' 

bp_cashback = Blueprint('cashback', __name__)

@bp_cashback.route('/api/cashback', methods=['POST'])
def cashback():
    try:
        order = validation(request)
    except exceptions.ValidationError as e:
        message = e.normalized_messages()
        return message, 400

    cashback = 0
    for product in order['products']:
        cashback += calculate_cashback(product)

    data = {'cashback': cashback, 'document': order['customer']['document']}
    response = send_request(data)

    return response.text, response.status_code 

def validation(request):
    os = OrderSchema()
    order = os.load(request.json)
    return order

def send_request(payload):
    response = requests.post(EXTERNAL_API_URL, data=payload)
    return response
