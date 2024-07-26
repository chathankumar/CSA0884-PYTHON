def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary
decimal = 10
binary = decimal_to_binary(decimal)
print(f"The binary representation of {decimal} is {binary}.")
