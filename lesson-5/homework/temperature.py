def convert_cel_to_far(celsius):
    """Converts Celsius to Fahrenheit."""
    return round(celsius * 9/5 + 32, 2)

def convert_far_to_cel(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return round((fahrenheit - 32) * 5/9, 2)

def main():
    try:
        # Prompt user for Fahrenheit input and convert to Celsius
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is {convert_far_to_cel(fahrenheit)}°C")

        # Prompt user for Celsius input and convert to Fahrenheit
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is {convert_cel_to_far(celsius)}°F")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Test cases for convert_cel_to_far()
print("Test Case 1: Convert 0°C to Fahrenheit")
print(convert_cel_to_far(0))  

# Test cases for convert_far_to_cel()
print("\nTest Case 6: Convert 32°F to Celsius (Freezing Point)")
print(convert_far_to_cel(32))  
