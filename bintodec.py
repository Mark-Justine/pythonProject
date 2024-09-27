def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        if digit == '1':
            decimal += 2 ** power
        elif digit != '0':
            return None # Invalid binary input
        power -= 1
    return decimal