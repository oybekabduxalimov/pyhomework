def factors(n):
    """Returns all factors of a given number n."""
    if n <= 0:
        raise ValueError("Please enter a positive integer.")

    result = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:  # Avoid duplicate factors when n is a perfect square
                result.append(n // i)
    return sorted(result)

def main():
    try:
        num = int(input("Enter a positive integer: "))
        factors_list = factors(num)
        print(f"Factors of {num}: {', '.join(map(str, factors_list))}")
    except ValueError as e:
        print(e)

# Test cases for factors function

print("Test Case 1: Factors of 12 (General Case)")
factors(12)  
# Expected output: 1, 12, 2, 6, 3, 4

print("\nTest Case 2: Factors of 25 (Perfect Square)")
factors(25)  
# Expected output: 1, 25, 5 (Avoids duplicate printing of 5)