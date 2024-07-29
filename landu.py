def create_tuples(lower, upper):
    return [(i, i**2) for i in range(lower, upper + 1)]
lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))
print(create_tuples(lower_range, upper_range))
 