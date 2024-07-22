def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
sample_list = [8, 2, 3, 0, 7] 
result = sum_list(sample_list)
print("Sum of the list:", result)
