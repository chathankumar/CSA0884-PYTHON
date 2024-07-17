def count_composite_numbers(array):
    def is_composite(n):
        if n < 4:
            return False
        if n % 2 == 0 or n % 3 == 0:
            return True
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return True
            i += 6
        return False
    return sum(map(is_composite, array))
array = [16, 18, 27, 16, 23, 21, 19]
print(f"Number of Composite Numbers = {count_composite_numbers(array)}")
