def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    # First convert to Celsius, then to Kelvin
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    # First convert to Celsius, then to Fahrenheit
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def format_result(value, decimal_places):
    """Format the result with the specified number of decimal places"""
    format_str = f"{{:.{decimal_places}f}}"
    return format_str.format(value)

def display_menu():
    """Display the menu of conversion options"""
    print("\nTemperature Unit Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("0. Exit program")

print("Welcome to the Temperature Unit Converter!")
decimal_places = 2  # Default decimal places

while True:
    display_menu()
    
    try:
        choice = int(input("\nEnter your choice (0-6): "))
        
        if choice == 0:
            print("Thank you for using the Temperature Unit Converter. Goodbye!")
            break
        
        if choice < 0 or choice > 6:
            print("Invalid choice! Please enter a number between 0 and 6.")
            continue
        
        # Ask for decimal places preference
        try:
            decimal_input = input(f"Enter number of decimal places (currently {decimal_places}, press Enter to keep): ")
            if decimal_input.strip():  # If user entered something
                new_decimal = int(decimal_input)
                if new_decimal < 0:
                    print("Cannot use negative decimal places. Keeping current setting.")
                else:
                    decimal_places = new_decimal
                    print(f"Decimal places set to {decimal_places}")
        except ValueError:
            print(f"Invalid input. Keeping decimal places at {decimal_places}.")
            
        if choice == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            result = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C = {format_result(result, decimal_places)}°F")
        elif choice == 2:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            result = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F = {format_result(result, decimal_places)}°C")
        elif choice == 3:
            celsius = float(input("Enter temperature in Celsius: "))
            result = celsius_to_kelvin(celsius)
            print(f"{celsius}°C = {format_result(result, decimal_places)}K")
        elif choice == 4:
            kelvin = float(input("Enter temperature in Kelvin: "))
            result = kelvin_to_celsius(kelvin)
            print(f"{kelvin}K = {format_result(result, decimal_places)}°C")
        elif choice == 5:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            result = fahrenheit_to_kelvin(fahrenheit)
            print(f"{fahrenheit}°F = {format_result(result, decimal_places)}K")
        elif choice == 6:
            kelvin = float(input("Enter temperature in Kelvin: "))
            result = kelvin_to_fahrenheit(kelvin)
            print(f"{kelvin}K = {format_result(result, decimal_places)}°F")
            
        input("\nPress Enter to continue...")
        
    except ValueError:
        print("Invalid input! Please enter a number.")