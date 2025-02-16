import numpy as np


def solve_linear_system(A, B):
    """
    Solves a system of linear equations Ax = B.
    :param A: Coefficient matrix (numpy array)
    :param B: Constant terms (numpy array)
    :return: Solution array if solvable, else None
    """
    try:
        return np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        print("Error: Singular or inconsistent matrix. No unique solution.")
        return None


if __name__ == "__main__":
    coefficient_matrix = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
    constant_terms = np.array([12, -5, 15])
    solutions = solve_linear_system(coefficient_matrix, constant_terms)

    if solutions is not None:
        print("System 2 Solutions (I1, I2, I3):", solutions)
