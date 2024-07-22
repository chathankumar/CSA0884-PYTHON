def multiply_matrices(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
A = [[2, 1], [3, 4]]
B = [[31, 1], [2, 2]]
C = multiply_matrices(A, B)
for row in C:
    print(row)
