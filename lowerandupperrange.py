def perfect_squares_in_range(lower, upper):
    return [i for i in range(lower, upper + 1) if int(i**0.5) ** 2 == i and sum(int(digit) for digit in str(i)) < 10]
lower_range = int(input("Enter lower range: "))
upper_range = int(input("Enter upper range: "))
print(perfect_squares_in_range(lower_range, upper_range))
