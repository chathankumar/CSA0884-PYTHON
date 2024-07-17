def sumsquare(l):
    odd_sum = 0
    even_sum = 0
    for num in l:
        if num % 2 == 0: 
            even_sum += num ** 2
        else:  
            odd_sum += num ** 2
    return [odd_sum, even_sum]
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    elements = []
    for _ in range(n):
        element = int(input("Enter the element: "))
        elements.append(element)
    result = sumsquare(elements)
    print(result)
