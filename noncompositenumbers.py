def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def find_primes(numbers):
    """Find all prime numbers in the list."""
    primes = [num for num in numbers if is_prime(num)]
    return primes
array_of_elements = [26, 28, 47, 26, 43, 51, 29]
prime_numbers = find_primes(array_of_elements)
print(f"Prime numbers in Array elements = {prime_numbers}")
