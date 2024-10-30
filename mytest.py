

def bob(A):
    n = len(A)
    for i in range(n):
        if n !=len(A[i]):
            return 1

    for i in range(n):
        if A[i][i] == 0:
            return 2


    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    # Perform LU decomposition
    for i in range(n):
        # Upper triangular matrix U
        for j in range(i, n):
            sum_u = 0.0
            for k in range(i):
                sum_u += L[i][k] * U[k][j]
            U[i][j] = A[i][j] - sum_u

        # Lower triangular matrix L
        for j in range(i, n):
            if i == j:
                L[i][i] = 1.0  # Diagonal as 1 in L
            else:
                sum_l = 0.0
                for k in range(i):
                    sum_l += L[j][k] * U[k][i]
                L[j][i] = (A[j][i] - sum_l) / U[i][i]

    return L, U,



A = [
    [4, 3, 2],
    [6, 3, 4],
    [2, 7, 3]
]

result=bob(A)


# Check if the result is valid or if there's an error
if result == 1:
    print("Error: The matrix is not square.")
elif result == 2:
    print("Error: The matrix has a zero on the diagonal.")
else:
    L, U = result
    print("L matrix:")
    for row in L:
        print(row)

    print("\nU matrix:")
    for row in U:
        print(row)