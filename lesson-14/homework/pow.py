import numpy as np


def power_function(base, exponent):
    """
    Computes the power of base raised to exponent.
    :param base: Base number
    :param exponent: Exponent number
    :return: base ** exponent
    """
    try:
        base, exponent = float(base), float(exponent)
        return base ** exponent
    except ValueError:
        print("Error: Invalid input. Please enter numerical values.")
        return None


if __name__ == "__main__":
    bases = np.array([2, 3, 4, 5])
    exponents = np.array([1, 2, 3, 4])
    power_results = np.power(bases, exponents)  # More efficient than vectorizing a custom function

    print("Power Results:", power_results)
