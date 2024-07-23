def main():
    matrix = [
        [4, 6, 7, 8],   
        [3, 7, 2, 7],   
        [7, 3, 7, 5]
    ]
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print("Original Matrix:")
    for row in matrix:
        print(row)
    print("\nTransposed Matrix:")
    for row in transposed:
        print(row)
if __name__ == "__main__":
    main()
