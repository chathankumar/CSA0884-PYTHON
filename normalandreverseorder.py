word = input("Enter the word: ")
word = word.upper()
sorted_letters = sorted(word)
reverse_sorted_letters = sorted_letters[::-1]
print(f"Alphabetical Order Normal: {' '.join(sorted_letters)}")
print(f"Alphabetical Order Reverse: {' '.join(reverse_sorted_letters)}")
