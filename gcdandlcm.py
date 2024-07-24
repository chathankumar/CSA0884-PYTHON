import math
def gcd(a, b):
    return math.gcd(a, b)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
num1, num2 = 12, 15
print(f"GCD of {num1} and {num2} is: {gcd(num1, num2)}")
print(f"LCM of {num1} and {num2} is: {lcm(num1, num2)}")
