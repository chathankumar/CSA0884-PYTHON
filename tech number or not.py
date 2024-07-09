def is_tech_number(number):
    digits = list(map(int, str(number)))
    return len(digits) % 2 == 0 and sum(digits) % 2 == 0
if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if is_tech_number(number):
            print(f"{number} is a Tech number.")
        else:
            print(f"{number} is not a Tech number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
