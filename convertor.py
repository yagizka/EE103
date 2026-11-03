def binary_convertor(number):
    if number == 0:
        return "0"

    binary = ""
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2

    return binary