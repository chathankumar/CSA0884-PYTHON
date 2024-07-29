def nth_largest(numbers, N):
    return sorted(numbers, reverse=True)[N-1]
numbers = [14, 67, 48, 23, 5, 62]
N = int(input("Enter the value of N: "))
print(f"{N}th Largest number: {nth_largest(numbers, N)}")
