def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = 7
result = check_odd_even(number)
print(f"The number {number} is {result}.")
