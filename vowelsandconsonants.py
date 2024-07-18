statement = input("Enter the statement: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for char in statement:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"Number of vowels = {vowel_count}")
print(f"Number of consonants = {consonant_count}")
print("Vowels are in the majority." if vowel_count > consonant_count else "Consonants are in the majority." if consonant_count > vowel_count else "Vowels and consonants are equal.")
