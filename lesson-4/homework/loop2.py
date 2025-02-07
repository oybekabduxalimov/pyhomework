def squared(n):
    # Validate input
    if not isinstance(n, int) or n < 1:
        print("Invalid input. Provide a positive integer.")
        return
    # Print squares of numbers from 1 to n-1
    print("\n".join(str(i**2) for i in range(1, n)))
