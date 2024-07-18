input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ''.join(char for char in input_string if char not in vowels)
print("The string without vowels is:", result)
