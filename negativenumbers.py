list_of_elements = [16, -18, 27, -16, 23, -21, 19]
negative_count = 0
for number in list_of_elements:
    if number < 0:
        negative_count += 1
print(f"Number of negative numbers in List of elements = {negative_count}")
