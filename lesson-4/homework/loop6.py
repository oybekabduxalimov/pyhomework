import math

def print_primes():
    def is_prime(n):
        # Check if number is prime using sqrt optimization
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    # Generate and print prime numbers from 1 to 100
    primes = [str(num) for num in range(1, 101) if is_prime(num)]
    print(" ".join(primes))

print_primes()
