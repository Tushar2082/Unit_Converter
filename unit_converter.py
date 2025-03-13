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
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def display_menu():
    """Display the menu of conversion options"""
    print("\nTemperature Unit Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Set default values")
    print("0. Exit program")

print("Welcome to the Simple Temperature Unit Converter!")

# Default values
default_c = 25.0  # Room temperature in Celsius
default_f = 72.0  # Room temperature in Fahrenheit
default_k = 298.15  # Room temperature in Kelvin

while True:
    display_menu()
    
    try:
        choice = input("\nEnter your choice (0-7): ")
        
        if choice == "0":
            print("Thank you for using the Temperature Unit Converter. Goodbye!")
            break
            
        if choice == "7":
            print("\nSet Default Values")
            try:
                new_c = input(f"Default Celsius value (current: {default_c}): ")
                if new_c:
                    default_c = float(new_c)
                    
                new_f = input(f"Default Fahrenheit value (current: {default_f}): ")
                if new_f:
                    default_f = float(new_f)
                    
                new_k = input(f"Default Kelvin value (current: {default_k}): ")
                if new_k:
                    default_k = float(new_k)
                    
                print("Default values updated!")
            except ValueError:
                print("Invalid input. Using previous default values.")
            continue
            
        if choice == "1":
            temp_input = input(f"Enter temperature in Celsius (default: {default_c}): ")
            celsius = default_c if temp_input == "" else float(temp_input)
            result = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C = {result:.2f}°F")
            
        elif choice == "2":
            temp_input = input(f"Enter temperature in Fahrenheit (default: {default_f}): ")
            fahrenheit = default_f if temp_input == "" else float(temp_input)
            result = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F = {result:.2f}°C")
            
        elif choice == "3":
            temp_input = input(f"Enter temperature in Celsius (default: {default_c}): ")
            celsius = default_c if temp_input == "" else float(temp_input)
            result = celsius_to_kelvin(celsius)
            print(f"{celsius}°C = {result:.2f}K")
            
        elif choice == "4":
            temp_input = input(f"Enter temperature in Kelvin (default: {default_k}): ")
            kelvin = default_k if temp_input == "" else float(temp_input)
            result = kelvin_to_celsius(kelvin)
            print(f"{kelvin}K = {result:.2f}°C")
            
        elif choice == "5":
            temp_input = input(f"Enter temperature in Fahrenheit (default: {default_f}): ")
            fahrenheit = default_f if temp_input == "" else float(temp_input)
            result = fahrenheit_to_kelvin(fahrenheit)
            print(f"{fahrenheit}°F = {result:.2f}K")
            
        elif choice == "6":
            temp_input = input(f"Enter temperature in Kelvin (default: {default_k}): ")
            kelvin = default_k if temp_input == "" else float(temp_input)
            result = kelvin_to_fahrenheit(kelvin)
            print(f"{kelvin}K = {result:.2f}°F")
            
        else:
            print("Invalid choice! Please enter a number between 0 and 7.")
            continue
            
        input("\nPress Enter to continue...")
        
    except ValueError:
        print("Invalid input! Please enter a number.")
