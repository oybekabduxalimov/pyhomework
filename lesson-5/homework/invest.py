def invest(amount, rate, years):
    """Calculates and prints investment growth over a given number of years."""
    for year in range(1, years + 1):
        amount *= (1 + rate / 100)  # Correct compound interest formula
        print(f"Year {year}: ${amount:.2f}")  # Format output to 2 decimal places

def main():
    try:
        # Prompt user for investment details
        initial_amount = float(input("Enter initial investment amount: "))
        annual_rate = float(input("Enter annual interest rate (in %): "))
        years = int(input("Enter number of years: "))

        # Validate inputs
        if initial_amount < 0 or annual_rate < 0 or years <= 0:
            print("Please enter positive values for all inputs.")
            return
        
        # Call the function with user inputs
        invest(initial_amount, annual_rate, years)

    except ValueError:
        print("Invalid input! Please enter numerical values.")

print("Test Case 1: Standard Investment Growth")
invest(1000, 5, 3)  

print("\nTest Case 2: High Interest Rate")
invest(500, 20, 2)  
