import requests


from flask import request


from .serializers import OrderSchema
from .settings import EXTERNAL_API_URL


def validation(request):
    os = OrderSchema()
    order = os.load(request.json)

    return order


def validate_request(response):
    if response.status_code != 201:
        raise Exception("Request to external API did not return 201 Created as expected")

    return response


def send_request(payload):
    response = requests.post(EXTERNAL_API_URL, data=payload)
    response = validate_request(response)

    return response
