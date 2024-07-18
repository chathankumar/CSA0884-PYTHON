def are_isomorphic(s, t):
    return (len(s) == len(t) and
            len(set(zip(s, t))) == len(set(s)) == len(set(t)))
s = "egg"
t = "add"
print(are_isomorphic(s, t))
