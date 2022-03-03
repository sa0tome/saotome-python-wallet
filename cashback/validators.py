from .utils import TYPE_CASHBACK

def validate_type(value):
    if value not in TYPE_CASHBACK.keys():
        raise ValidationError("Invalid type")

def validate_cpf(value):
    first_digit = calculate_digits(value[:9])
    second_digit = calculate_digits(value[:10])
    if first_digit != int(value[9]) or second_digit != int(value[10]):
        raise ValidationError("Invalid CPF")

def calculate_digits(sequence):
    n = len(sequence) + 1
    total_sum = 0
    for i in range(n - 1):
        total_sum += int(sequence[i])*n
        n -= 1
    if 0 <= total_sum % 11 <= 1:
        return 0
    return 11 - (total_sum % 11)
