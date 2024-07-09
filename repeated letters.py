def find_repeated_letters(word):
    repeated_letters = set()
    seen_letters = set()
    for char in word:
        if char in seen_letters:
            repeated_letters.add(char)
        else:
            seen_letters.add(char)
    print(f"Number of repeated letters = {len(repeated_letters)}")
    if repeated_letters:
        print(f"Repeated letter(s) = {' '.join(sorted(repeated_letters))}")
if __name__ == "__main__":
    word = input("Enter the word: ").upper() 
    find_repeated_letters(word)
