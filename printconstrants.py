def main():
    fruit_quantities = {
        "Apple": 5,
        "Orange": 10,
        "Banana": 12
    }
    print("Contents of the dictionary:")
    for fruit, quantity in fruit_quantities.items():
        print(f"{fruit} : {quantity}")
if __name__ == "__main__":
    main()
