def linear_search(lst, target):
    for element in lst:
        if element == target:
            return "Exist"
    return "not exist"
def main():
    input_list = [2, 4, 6, 8, 9, 7, 9]
    targets = [7, 5]
    for target in targets:
        result = linear_search(input_list, target)
        print(f"Target: {target}\nResult: {result}\n")

if __name__ == "__main__":
    main()
