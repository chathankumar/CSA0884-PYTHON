def find_duplicates(input_list):
    duplicates = list(set([element for element in input_list if input_list.count(element) > 1]))
    return duplicates
input_list = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 9, 2]
duplicates = find_duplicates(input_list)
print("Duplicate elements:", duplicates)
