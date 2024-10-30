def kaka_sardar(A):
    # Get matrix size
    n = len(A)

    #check if the matrix is square
    for i in range(0, n):
        if n != len(A[i]):
            raise ValueError("Matrix must be square")

    #check if the matrix has zero in the diagonal
    for i in range(0, n):
        if A[i][i] == 0:    # Changed != to ==
            raise ValueError("Matrix must not have zeros on diagonal")

    # Initialize L and U matrices with zeros
    L = [[0.0] * n for i in range(n)]    # Fixed syntax
    U = [[0.0] * n for i in range(n)]    # Fixed syntax

    # the U part
    for row in range(0, n):
        for col in range(0, n):
            if row > col:
                for k in range(0, n):
                        U[row][k] = A[row][k] - ( A[col][k] * ((A[row][col]) / (A[col][col])) )

    #the L part
    for row in range(0, n):
        for col in range(0, n):
            #make diagonal to 1
            L[row][row] = 1

            if row > col:    # Fixed comparison
                for k in range(0, n):
                    L[row][col] = A[row][col] / A[col][col]

    # retrivel the L and U matrices
    return L, U



# Example usage
A = [
    [1, 2, 3],
    [2, 5, 8],
    [3, 8, 14]
]

L, U = kaka_sardar(A)
print("Upper Triangular (U):\n")
for row in U:
    print(row)
print("\n")
print("Lower Triangular (L):\n")
for row in L:
    print(row)