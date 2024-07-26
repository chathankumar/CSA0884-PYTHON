def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
def calculate_compound_interest(principal, rate, time, n):
    amount = principal * (1 + (rate / (n * 100))) ** (n * time)
    return amount - principal
principal = 1000 
rate = 5  
time = 3 
n = 4
simple_interest = calculate_simple_interest(principal, rate, time)
compound_interest = calculate_compound_interest(principal, rate, time, n)
print(f"Simple Interest: {simple_interest}")
print(f"Compound Interest: {compound_interest}")
