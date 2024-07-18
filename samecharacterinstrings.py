def count_matching_indices(s1, s2):
    min_length = min(len(s1), len(s2))
    matches = sum(1 for i in range(min_length) if s1[i] == s2[i])
    return matches
s1 = "what"
s2 = "watch which"
print(count_matching_indices(s1, s2))
