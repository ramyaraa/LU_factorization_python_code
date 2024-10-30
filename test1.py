import numpy as np
import scipy.linalg

def format_matrix(name, matrix):
    """Print matrix with simple one decimal point format."""
    print(f"\n{name}:")
    # Convert to array in case input is a matrix
    matrix = np.asarray(matrix)
    # Round to 1 decimal place and convert to string format
    formatted = np.array2string(
        matrix,
        precision=1,
        suppress_small=True,
        floatmode='fixed',
        separator=', ',
        formatter={'float_kind': lambda x: f"{x:.1f}"}
    )
    print(formatted)

def main():
    # Input matrix
    A = np.array([
        [7, 3, -1, 2],
        [3, 8, 1, -4],
        [-1, 1, 4, -1],
        [2, -4, -1, 6]
    ])

    # Perform LU decomposition
    P, L, U = scipy.linalg.lu(A)

    # Print each matrix with simple formatting
    format_matrix("A", A)
    format_matrix("P", P)
    format_matrix("L", L)
    format_matrix("U", U)

if __name__ == "__main__":
    main()