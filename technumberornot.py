def is_tech_number(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return (int(s[:half]) ** 2 + int(s[half:]) ** 2) == n
number = 3025
print(f"{number} is {'a Tech number' if is_tech_number(number) else 'not a Tech number'}.")
