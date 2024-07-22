def kilometers_to_miles(kilometers):
    conversion_factor = 0.621371
    miles = kilometers * conversion_factor
    return miles
kilometers = 5
miles = kilometers_to_miles(kilometers)
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
