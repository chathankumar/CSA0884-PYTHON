def is_armstrong_number(n):
    digits = [int(d) for d in str(n)]
    return n == sum(d ** len(digits) for d in digits)
number = 153
print(f"{number} is {'an Armstrong number' if is_armstrong_number(number) else 'not an Armstrong number'}.")
