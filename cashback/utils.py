from decimal import *

TYPE_CASHBACK = {'A': 0.15, 'B': 0.10, 'C': 0.05}

def calculate_cashback(product):
    total = Decimal(product['value'])*product['qty']
    for key, value in TYPE_CASHBACK.items():
        if key == product['type']:
            return Decimal(value)*total
