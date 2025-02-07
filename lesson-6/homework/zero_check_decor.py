import logging

def check(func):
    """Decorator to check if the denominator is zero before division."""
    def wrapper(a, b):
        if b == 0:
            logging.error("Attempted division by zero.")
            raise ValueError("Error: Denominator can't be zero.")
        return func(a, b)
    return wrapper

@check
def div(a, b):
    """Performs division of two numbers."""
    return a / b

if __name__ == "__main__":
    try:
        print(div(6, 2))  # Output: 3.0
        print(div(6, 0))  # Raises ValueError
    except ValueError as e:
        print(e)
