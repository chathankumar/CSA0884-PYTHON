
remove_duplicates = lambda lst: list(dict.fromkeys(lst))
if __name__ == "__main__":
    try:
        lst = input("Enter elements of the list separated by spaces: ").split()
        result = remove_duplicates(lst)
        print(f"List with duplicates removed: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid list of elements.")
