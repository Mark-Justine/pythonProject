def decimal_to_binary(decimal_num):
    binary_num = ''

    if decimal_num < 0:
        binary_num += '1'
        decimal_num = abs(decimal_num)
    else:
        binary_num += '0'

    if decimal_num == 0:
        return '0'

    while decimal_num > 0:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num = decimal_num // 2

    return binary_num


