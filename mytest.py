

def lu_factorization(A):

    #check if the matrix is square
    # for i in range(n):
    #     if len(A[i]) != n:

    n = len(A)
    L = [[0 for _ in range(n)] for _ in range(n)]

    for row in range(n):
        L[row][row] = 1
        for col in range(row+1, n):
            L[row][col] = A[row][col] / A[row][row]
            for i in range(col, n):
                A[col][i] -= L[row][col] * A[row][i]

    print(L)
  # loop through the matrix





A = [
    [1, 1, 1],
    [4, 3, -1],
    [3, 5, 3],
]

lu_factorization(A)
