import math

def is_prime(n):
    """Returns True if n is a prime number, otherwise returns False."""
    if n < 2:  
        return False  # 0 and 1 are not prime numbers
    if n in (2, 3):  
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:  
        return False  # Eliminate even numbers and multiples of 3
    
    # Check divisibility up to sqrt(n) using 6k ± 1 optimization
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    
    return True  # If no factors found, n is prime

# Test cases
print(is_prime(1))   # False
print(is_prime(2))   # True
print(is_prime(3))   # True
print(is_prime(4))   # False