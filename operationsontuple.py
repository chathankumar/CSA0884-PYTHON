tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
element_to_search = 3
index_of_element = concatenated_tuple.index(element_to_search)
count_of_element = concatenated_tuple.count(element_to_search)
print("Concatenated tuple =", concatenated_tuple)
print("Index of element", element_to_search, ":", index_of_element)
print("Number of occurrences of element", element_to_search, "is:", count_of_element)
