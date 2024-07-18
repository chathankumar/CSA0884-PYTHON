input_string = input("Enter the string: ")
char_to_search = input("Enter the character to be searched: ")
if len(char_to_search) != 1:
    print("Please enter exactly one character.")
else:
    found = False
    for index in range(len(input_string)):
        if input_string[index] == char_to_search:
            print(f"{char_to_search} is found in string at index: {index}")
            found = True
            break  
    if not found:
        print(f"{char_to_search} is not found in the string.")
