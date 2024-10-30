def lu_factorization(matrix):
    n = len(matrix)
    # Create an empty lower matrix initialized to identity
    lower = [[0 for _ in range(n)] for _ in range(n)]

    # Initialize the diagonal of the lower matrix to 1
    for i in range(n):
        lower[i][i] = 1

    # Perform Gaussian elimination to convert the matrix to an upper triangular form
    for k in range(n):
        # Ensure the pivot is not zero (no row swapping in this implementation)
        for i in range(k+1, n):
            # Find the multiplier for row operations
            factor = matrix[i][k] / matrix[k][k]
            lower[i][k] = factor
            print(lower[i][k])

            # Eliminate the current column entries below the pivot
            for j in range(k, n):
                matrix[i][j] -= factor * matrix[k][j]

    return lower, matrix  # matrix is now the upper matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)

# Example usage
A = [
    [1, 1, 1],
    [4, 3, -1],
    [3, 5, 3]
]

L, U = lu_factorization(A)

print("Lower Matrix (L):")
print_matrix(L)

print("Upper Matrix (U):")
print_matrix(U)
