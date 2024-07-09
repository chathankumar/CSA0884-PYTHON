if __name__ == "__main__":
    try:
        input_string = input("Enter a string: ")
        letter_count = sum(1 for char in input_string if char.isalpha())
        digit_count = sum(1 for char in input_string if char.isdigit())
        print(f"Letters {letter_count}")
        print(f"Digits {digit_count}")
    except ValueError:
        print("Invalid input. Please enter a valid string.")
