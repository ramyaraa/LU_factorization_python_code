import numpy as np
import scipy.linalg

def is_integer(x):
    """Check if a number is effectively an integer."""
    return np.abs(x - round(x)) < 1e-10

def format_number(x):
    """Format number: integers without decimal, others with one decimal."""
    if is_integer(x):
        return f"{int(x)}"
    return f"{x:.1f}"

def format_matrix(name, matrix):
    """Print matrix with beautiful formatting."""
    # Convert to numpy array if not already
    matrix = np.asarray(matrix)

    # Get the maximum width needed for any number in the matrix
    formatted_elements = [[format_number(x) for x in row] for row in matrix]
    max_width = max(len(x) for row in formatted_elements for x in row)

    # Create the box drawing characters
    top_border    = "┌" + "─" * (max_width * matrix.shape[1] + 3 * (matrix.shape[1] - 1)) + "┐"
    bottom_border = "└" + "─" * (max_width * matrix.shape[1] + 3 * (matrix.shape[1] - 1)) + "┘"

    # Print the matrix with nice formatting
    print(f"\n{name}:")
    print(top_border)

    for row in formatted_elements:
        formatted_row = " │ ".join(f"{x:>{max_width}}" for x in row)
        print(f"│ {formatted_row} │")

    print(bottom_border)

def main():
    # Create a title banner
    print("\n" + "═" * 50)
    print("           LU DECOMPOSITION RESULTS")
    print("═" * 50)

    # Input matrix
    A = np.array([
        [7, 3, -1, 2],
        [3, 8, 1, -4],
        [-1, 1, 4, -1],
        [2, -4, -1, 6]
    ])

    # Perform LU decomposition
    P, L, U = scipy.linalg.lu(A)

    # Print each matrix with beautiful formatting
    format_matrix("Original Matrix (A)", A)
    format_matrix("Permutation Matrix (P)", P)
    format_matrix("Lower Triangular Matrix (L)", L)
    format_matrix("Upper Triangular Matrix (U)", U)

    # Add verification footer
    print("\n" + "─" * 50)
    print("Verification: PA = LU")
    PA = P @ A
    LU = L @ U
    max_error = np.max(np.abs(PA - LU))
    print(f"Maximum error: {max_error:.2e}")
    print("─" * 50 + "\n")

if __name__ == "__main__":
    main()