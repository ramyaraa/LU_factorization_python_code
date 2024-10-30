import numpy as np
import scipy.linalg
import numpy.testing as npt

def perform_lu_decomposition(A):
    """
    Perform LU decomposition using SciPy and validate results.

    Args:
        A: Input matrix as numpy array

    Returns:
        Tuple of (P, L, U) matrices and verification results
    """
    # Convert to float for better numerical stability
    A = np.array(A, dtype=float)

    # Perform LU decomposition
    P, L, U = scipy.linalg.lu(A)

    # Verify the decomposition
    PA = P @ A
    LU = L @ U

    # Check if PA = LU
    try:
        npt.assert_almost_equal(PA, LU, decimal=10)
        verification = "✓ Verified: PA = LU"
    except AssertionError:
        verification = "✗ Warning: PA ≠ LU (numerical differences found)"

    # Check properties of L and U
    is_L_lower = np.allclose(L, np.tril(L))
    is_U_upper = np.allclose(U, np.triu(U))

    properties = [
        f"✓ L is lower triangular" if is_L_lower else "✗ L is not lower triangular",
        f"✓ U is upper triangular" if is_U_upper else "✗ U is not upper triangular",
        f"✓ L diagonal is 1" if np.allclose(np.diag(L), 1) else "✗ L diagonal is not 1",
        f"✓ P is permutation" if np.allclose(P @ P.T, np.eye(len(P))) else "✗ P is not permutation"
    ]

    return P, L, U, verification, properties

def format_matrix(name, matrix, precision=4):
    """Pretty print a matrix with name and properties."""
    format_str = f"{precision+6}.{precision}f"
    header = f"\n{name}:"
    matrix_str = np.array2string(matrix,
                                 precision=precision,
                                 floatmode='fixed',
                                 suppress_small=True,
                                 separator=', ',
                                 formatter={'float_kind': lambda x: f"{x:{format_str}}"})
    return header + "\n" + matrix_str

def main():
    # Input matrix
    A = np.array([
        [7, 3, -1, 2],
        [3, 8, 1, -4],
        [-1, 1, 4, -1],
        [2, -4, -1, 6]
    ])

    # Perform decomposition and verification
    P, L, U, verification, properties = perform_lu_decomposition(A)

    # Print results with formatting
    print("\nLU Decomposition Analysis")
    print("=" * 50)

    # Print matrices
    for name, matrix in [("A", A), ("P", P), ("L", L), ("U", U)]:
        print(format_matrix(name, matrix))

    # Print verification results
    print("\nVerification Results:")
    print("=" * 50)
    print(verification)

    # Print matrix properties
    print("\nMatrix Properties:")
    print("=" * 50)
    for prop in properties:
        print(prop)

    # Print additional checks
    print("\nNumerical Properties:")
    print("=" * 50)
    print(f"Matrix condition number: {np.linalg.cond(A):.2e}")
    print(f"Max absolute error in PA=LU: {np.max(np.abs(P @ A - L @ U)):.2e}")

if __name__ == "__main__":
    main()