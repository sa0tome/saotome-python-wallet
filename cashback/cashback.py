from flask import Blueprint, request
from flask_httpauth import HTTPTokenAuth
from marshmallow import exceptions


from .utils import calculate_cashback, decode_token
from .utils_cashback import validation, validate_request, send_request
from .settings import WALLET_SECRET


bp_cashback = Blueprint("cashback", __name__)
auth = HTTPTokenAuth("Token")


@auth.verify_token
def verify_token(token):
    token = decode_token(token)
    
    return token == WALLET_SECRET


@bp_cashback.route("/api/cashback", methods=["POST"])
@auth.login_required
def cashback():
    try:
        order = validation(request)
    except exceptions.ValidationError as e:
        message = e.normalized_messages()

        return message, 400

    cashback = 0
    for product in order["products"]:
        cashback += calculate_cashback(product)

    data = {"cashback": cashback, "document": order["customer"]["document"]}

    try:
        response = send_request(data)
    except Exception as e:
        message = str(e)

        return {"response from external API": message}, 400
         
    return response.json(), response.status_code 

