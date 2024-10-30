import numpy as np

def lu_factorization(matrix):
    n = len(matrix)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    # Perform LU Factorization
    for i in range(n):
        # Upper Triangular (U)
        for j in range(i, n):
            U[i][j] = matrix[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

        # Lower Triangular (L)
        L[i][i] = 1  # Diagonal as 1
        for j in range(i + 1, n):
            L[j][i] = (matrix[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U

def print_matrix(matrix, name):
    print(f"{name} Matrix:")
    for row in matrix:
        print(" ".join(f"{val:.2f}" for val in row))
    print()

# Example usage
matrix = [
    [4, 3, 2],
    [6, 3,-1],
    [2, 5, 8]
]

L, U = lu_factorization(matrix)
print_matrix(L, "Lower Triangular (L)")
print_matrix(U, "Upper Triangular (U)")
