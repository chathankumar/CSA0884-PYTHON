age = int(input("Enter the passenger's age: "))
if age <= 3:
    price = 0
elif 4 <= age <= 12:
    price = 10
else:
    price = 20
print("The ticket price is Rs", price)
