def print_evens_before_20(numbers):
    for number in numbers:
        if number == 20:
            break
        if number % 2 == 0:
            print(number)
numbers_list = [3, 5, 8, 12, 17, 20, 22, 24]
print_evens_before_20(numbers_list)
