if __name__ == "__main__":
    try:
        series = list(map(int, input("Enter a series of numbers separated by spaces: ").split()))
        even_count = sum(1 for num in series if num % 2 == 0)
        odd_count = len(series) - even_count
        print(f"Number of even numbers: {even_count}")
        print(f"Number of odd numbers: {odd_count}")
    except ValueError:
        print("Invalid input. Please enter a valid series of numbers.")
