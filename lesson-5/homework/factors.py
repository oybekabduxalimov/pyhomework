def factors(n):
    """Prints all factors of a given number n."""
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    for i in range(1, int(n ** 0.5) + 1):  # Only iterate up to sqrt(n) for efficiency
        if n % i == 0:
            print(f"{i} is a factor of {n}")
            if i != n // i:  # Avoid duplicate factors when n is a perfect square
                print(f"{n // i} is a factor of {n}")

def main():
    try:
        num = int(input("Enter a positive integer: "))
        factors(num)
    except ValueError:
        print("Invalid input! Please enter a valid positive integer.")

# Test cases for factors function

print("Test Case 1: Factors of 12 (General Case)")
factors(12)  
# Expected output: 1, 12, 2, 6, 3, 4

print("\nTest Case 2: Factors of 25 (Perfect Square)")
factors(25)  
# Expected output: 1, 25, 5 (Avoids duplicate printing of 5)