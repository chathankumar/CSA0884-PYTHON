def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def find_primes(arr):
    return [x for x in arr if is_prime(x)]
arr = [26, 28, 47, 26, 43, 51, 29]
print(f"Prime numbers in Array elements = {find_primes(arr)}")
