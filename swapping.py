def swap_with_temp_var(a, b):
    print(f"Original values: a = {a}, b = {b}")
    temp = a
    a = b
    b = temp
    print(f"Swapped values: a = {a}, b = {b}")
a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
swap_with_temp_var(a, b)
