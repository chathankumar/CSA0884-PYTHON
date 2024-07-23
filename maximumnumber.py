def find_maximum_binary(binaries):
    max_binary = max(binaries, key=lambda b: int(b, 2))
    return max_binary
def main():
    binary_numbers = ["1101", "1011", "1001"]
    max_binary = find_maximum_binary(binary_numbers)
    print(f"Maximum Number: {max_binary}")
if __name__ == "__main__":
    main()
