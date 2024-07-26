def check_positive_negative(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
number = -5
result = check_positive_negative(number)
print(f"The number {number} is {result}.")
