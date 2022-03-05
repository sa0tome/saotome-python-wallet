import requests
import base64


from decimal import Decimal


PRODUCT_TYPE_CASHBACK = {"A": 0.15, "B": 0.10, "C": 0.05}


def calculate_cashback(product):
    product_type = product["type"]
    value = product["value"]
    qty = product["qty"]
    total = value * qty 

    for i in PRODUCT_TYPE_CASHBACK:
        if i == product_type:
            return total * Decimal(PRODUCT_TYPE_CASHBACK[i])


def decode_token(token):
    binary = base64.b64decode(token)
    string = binary.decode("utf-8")

    return string
