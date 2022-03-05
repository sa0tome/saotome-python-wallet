from marshmallow.exceptions import ValidationError


from .utils import PRODUCT_TYPE_CASHBACK


def calculate_digits(sequence):
    n = len(sequence) + 1
    total_sum = 0

    for i in sequence:
        total_sum += int(i) * n
        n -= 1

    modulus = total_sum % 11
    if modulus in (0, 1):
        return 0

    return 11 - modulus


def validate_cpf(value):
    if len(value) != 11:
        raise ValidationError("Invalid CPF")

    first_digit = calculate_digits(value[:9])
    second_digit = calculate_digits(value[:10])

    if first_digit != int(value[9]) or second_digit != int(value[10]):
        raise ValidationError("Invalid CPF")


def validate_type(value):
    if value not in PRODUCT_TYPE_CASHBACK:
        raise ValidationError("Invalid product type")


def validate_value(value):
    if value < 0:
        raise ValidationError("Value cannot be negative")
