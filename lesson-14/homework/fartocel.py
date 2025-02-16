import numpy as np


def fahrenheit_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius.
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    try:
        return (float(fahrenheit) - 32) * 5 / 9
    except ValueError:
        print("Error: Invalid input. Please enter a numerical value.")
        return None


if __name__ == "__main__":
    temperatures_f = np.array([32, 68, 100, 212, 77])
    temperatures_c = np.vectorize(fahrenheit_to_celsius)(temperatures_f)

    print("Celsius Temperatures:", temperatures_c)
