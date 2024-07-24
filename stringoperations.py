def string_operations(str1, str2, start, end):
    concatenated = str1 + str2
    reversed_str = concatenated[::-1]
    sliced_str = concatenated[start:end]
    length_of_str = len(concatenated)
    return concatenated, reversed_str, sliced_str, length_of_str
str1 = "Hello"
str2 = "World"
start, end = 1, 8
concatenated, reversed_str, sliced_str, length_of_str = string_operations(str1, str2, start, end)
print("Concatenated string:", concatenated)
print("Reversed string:", reversed_str)
print("Sliced string:", sliced_str)
print("Length of string:", length_of_str)
