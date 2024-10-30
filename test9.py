def lu_decomposition(A):
    """
    Performs LU decomposition on a square matrix A.
    Returns lower triangular matrix L and upper triangular matrix U such that A = L * U.

    Args:
        A (list of lists): Square matrix to decompose

    Returns:
        tuple: (L, U) where L is lower triangular and U is upper triangular
    """
    # Get matrix size
    n = len(A)

    # Check if the matrix is square
    if not all(len(row) == n for row in A):
        raise ValueError("Matrix must be square")

    # Check if the matrix has zeros on the diagonal
    if any(A[i][i] == 0 for i in range(n)):
        raise ValueError("Matrix must not have zeros on diagonal")

    # Initialize L and U matrices with zeros
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    # Initialize U with the first row of A
    for j in range(n):
        U[0][j] = A[0][j]

    # Initialize L's diagonal with 1's and first column
    for i in range(n):
        L[i][i] = 1.0
        if i > 0:
            L[i][0] = A[i][0] / U[0][0]

    # Compute L and U entries
    for j in range(1, n):
        # Compute U's j-th row
        for k in range(j, n):
            sum_uk = sum(L[j][p] * U[p][k] for p in range(j))
            U[j][k] = A[j][k] - sum_uk

        # Compute L's j-th column
        for i in range(j + 1, n):
            sum_lk = sum(L[i][p] * U[p][j] for p in range(j))
            L[i][j] = (A[i][j] - sum_lk) / U[j][j]

    return L, U

def print_matrix(matrix, name):
    """Helper function to print matrices in a readable format"""
    print(f"{name}:")
    for row in matrix:
        print([f"{x:8.3f}" for x in row])
    print()

# Example usage
A = [
    [1, 2, 3],
    [2, 5, 8],
    [3, 8, 14]
]

L, U = lu_decomposition(A)
print_matrix(L, "Lower Triangular (L)")
print_matrix(U, "Upper Triangular (U)")

# Verify the decomposition
def matrix_multiply(A, B):
    """Helper function to multiply two matrices"""
    n = len(A)
    result = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return result

# Check if L * U = A
result = matrix_multiply(L, U)
print("Verification (L * U):")
print_matrix(result, "L * U")