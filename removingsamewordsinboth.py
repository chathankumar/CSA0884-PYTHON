def remove_common_words(s1, s2):
    words_s1 = set(s1.split())
    words_s2 = set(s2.split())
    common_words = words_s1.intersection(words_s2)
    filtered_s1 = ' '.join(word for word in s1.split() if word not in common_words)
    filtered_s2 = ' '.join(word for word in s2.split() if word not in common_words)
    print(filtered_s1)
    print(filtered_s2)
s1 = "sky is blue in color"
s2 = "Raj likes sky blue color"
remove_common_words(s1, s2)
