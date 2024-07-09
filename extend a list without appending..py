if __name__ == "__main__":
    try:
        list1 = [10, 20, 30]
        list2 = [40, 50, 60]
        extended_list = list2 + list1
        print(extended_list)
    except ValueError:
        print("Invalid input. Please enter valid lists.")
