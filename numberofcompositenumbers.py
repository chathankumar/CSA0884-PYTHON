def is_composite(n):
    return n > 1 and any(n % i == 0 for i in range(2, int(n**0.5) + 1))
def count_composites(arr):
    return sum(is_composite(x) for x in arr)
arr = [16, 18, 27, 16, 23, 21, 19]
print(f"Number of Composite Numbers = {count_composites(arr)}")
