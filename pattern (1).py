def print_patterns():
    print("Pattern 1:")
    for i in range(1, 6):
        print(" ".join(str(j) for j in range(1, i + 1)))
    print()
    print("Pattern 2:")
    for i in range(1, 6):
        print(" ".join(str(i) for _ in range(i)))
    print()
    print("Pattern 3:")
    for i in range(1, 6):
        print(" ".join(str(j * 10) for j in range(1, i + 1)))
    print()
    print("Pattern 4:")
    for i in range(1, 6):
        print(" ".join(f"{j/10:.1f}" for j in range(1, i + 1)))
    print()
    print("Pattern 5:")
    for i in range(1, 6):
        print(" ".join(str(5) for _ in range(i)))
    print()
print_patterns()
