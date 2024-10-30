from typing import List, Tuple
import pprint
from typing import Union
import numpy as np

Matrix = List[List[float]]

def format_matrix(matrix: Matrix, precision: int = 4) -> str:
    """
    Format a matrix for pretty printing with aligned columns.

    Args:
        matrix: The matrix to format
        precision: Number of decimal places to show

    Returns:
        Formatted string representation of the matrix
    """
    return '\n'.join([
        '[' + ' '.join(f'{x:>{precision + 3}.{precision}f}' for x in row) + ']'
        for row in matrix
    ])

def is_square_matrix(matrix: Matrix) -> bool:
    """
    Check if a matrix is square and well-formed.

    Args:
        matrix: Matrix to check

    Returns:
        True if matrix is square and well-formed, False otherwise
    """
    if not matrix or not isinstance(matrix, list):
        return False
    n = len(matrix)
    return all(isinstance(row, list) and len(row) == n for row in matrix)

def mult_matrix(M: Matrix, N: Matrix) -> Matrix:
    """
    Multiply two square matrices of same dimension.

    Args:
        M: First matrix
        N: Second matrix

    Returns:
        Result of matrix multiplication

    Raises:
        ValueError: If matrices are not square or have incompatible dimensions
    """
    if not is_square_matrix(M) or not is_square_matrix(N):
        raise ValueError("Inputs must be square matrices")
    if len(M) != len(N):
        raise ValueError("Matrices must have same dimensions")

    tuple_N = list(zip(*N))
    return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n))
             for col_n in tuple_N] for row_m in M]

def pivot_matrix(M: Matrix) -> Matrix:
    """
    Returns the pivoting matrix for M, used in Doolittle's method.

    Args:
        M: Input matrix

    Returns:
        Pivoting matrix P such that PA will use the maximum valued elements
        as pivots

    Raises:
        ValueError: If input is not a square matrix
    """
    if not is_square_matrix(M):
        raise ValueError("Input must be a square matrix")

    m = len(M)
    id_mat = [[float(i == j) for i in range(m)] for j in range(m)]

    for j in range(m):
        row = max(range(j, m), key=lambda i: abs(M[i][j]))
        if j != row:
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]

    return id_mat

def verify_lu_decomposition(A: Matrix, P: Matrix, L: Matrix, U: Matrix,
                            tolerance: float = 1e-10) -> bool:
    """
    Verify that PA = LU holds true for the decomposition.

    Args:
        A: Original matrix
        P: Permutation matrix
        L: Lower triangular matrix
        U: Upper triangular matrix
        tolerance: Maximum allowed difference between PA and LU

    Returns:
        True if decomposition is valid, False otherwise
    """
    PA = mult_matrix(P, A)
    LU = mult_matrix(L, U)

    n = len(A)
    for i in range(n):
        for j in range(n):
            if abs(PA[i][j] - LU[i][j]) > tolerance:
                return False
    return True

def lu_decomposition(A: Matrix) -> Tuple[Matrix, Matrix, Matrix]:
    """
    Performs an LU Decomposition of A into PA = LU using Doolittle's method.

    Args:
        A: Square matrix to decompose

    Returns:
        Tuple of (P, L, U) where:
            P is the permutation matrix
            L is the lower triangular matrix
            U is the upper triangular matrix

    Raises:
        ValueError: If matrix is not square or a zero pivot is encountered
    """
    if not is_square_matrix(A):
        raise ValueError("Input must be a square matrix")

    n = len(A)
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]
    P = pivot_matrix(A)
    PA = mult_matrix(P, A)

    for j in range(n):
        L[j][j] = 1.0

        # Calculate U's values (upper triangular matrix)
        for i in range(j + 1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = PA[i][j] - s1

        # Check for zero pivot
        if abs(U[j][j]) < 1e-10:
            raise ValueError(f"Zero pivot encountered at U[{j}][{j}]")

        # Calculate L's values (lower triangular matrix)
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (PA[i][j] - s2) / U[j][j]

    return (P, L, U)

def main():
    # Example usage
    A = [
        [7, 3, -1, 2],
        [3, 8, 1, -4],
        [-1, 1, 4, -1],
        [2, -4, -1, 6]
    ]

    try:
        P, L, U = lu_decomposition(A)

        print("\nOriginal Matrix A:")
        print(format_matrix(A))

        print("\nPermutation Matrix P:")
        print(format_matrix(P))

        print("\nLower Triangular Matrix L:")
        print(format_matrix(L))

        print("\nUpper Triangular Matrix U:")
        print(format_matrix(U))

        # Verify the decomposition
        is_valid = verify_lu_decomposition(A, P, L, U)
        print(f"\nDecomposition is {'valid' if is_valid else 'invalid'}!")

        # Show that PA = LU
        PA = mult_matrix(P, A)
        LU = mult_matrix(L, U)

        print("\nPA:")
        print(format_matrix(PA))

        print("\nLU:")
        print(format_matrix(LU))

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()