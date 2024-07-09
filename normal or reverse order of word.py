def arrange_letters(word):
    letters = list(word)
    normal_order = ''.join(sorted(letters))
    reverse_order = ''.join(sorted(letters, reverse=True))
    
    return normal_order, reverse_order
if __name__ == "__main__":
    try:
        word = input("Enter the word: ").upper()
        normal, reverse = arrange_letters(word)
        print(f"Normal order: {normal}")
        print(f"Reverse order: {reverse}")
    
    except ValueError:
        print("Invalid input. Please enter a valid word.")
