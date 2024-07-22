def find_max_of_three(num1, num2, num3):
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    return max_num
num1 = 6
num2 = 9
num3 = 56
maximum_number = find_max_of_three(num1, num2, num3)
print(maximum_number)
