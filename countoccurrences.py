def count_occurrences(tup, target):
    return tup.count(target)
numbers = (3, 6, 8, 9, 8, 9, 12, 35, 8)
target_number = 8
count = count_occurrences(numbers, target_number)
print(count)
