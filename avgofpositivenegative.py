def calculate_averages():
    positive_numbers = []
    negative_numbers = []
    while True:
        try:
            num = float(input("Enter the number: "))
            if num == -1:
                break
            elif num > 0:
                positive_numbers.append(num)
            elif num < 0:
                negative_numbers.append(num)
        except ValueError:
            print("Please enter a valid number.")
    if positive_numbers:
        avg_positive = sum(positive_numbers) / len(positive_numbers)
    else:
        avg_positive = 0.0

    if negative_numbers:
        avg_negative = sum(negative_numbers) / len(negative_numbers)
    else:
        avg_negative = 0.0
    print(f"The average of negative numbers is: {avg_negative:.2f}")
    print(f"The average of positive numbers is: {avg_positive:.2f}")
calculate_averages()
