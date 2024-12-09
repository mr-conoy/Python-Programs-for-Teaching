# Main Menu Function
def main_menu():
    print("Binary-Denary Converter")
    print("1. Convert Binary to Denary")
    print("2. Convert Denary to Binary")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    return choice

# Binary to Denary Conversion with Validation
def binary_to_denary(binary_str):
    # Validate input: ensure it's a binary number
    if not all(char in "01" for char in binary_str):
        return "Error: Input is not a valid binary number."
    return int(binary_str, 2)

# Denary to Binary Conversion with Validation
def denary_to_binary(denary_int):
    # Validate input: ensure it's a positive integer
    if not isinstance(denary_int, int) or denary_int < 0:
        return "Error: Input is not a valid positive integer."
    return bin(denary_int)[2:]

# Main Program with Error Handling and Repeat Option
def converter_program():
    while True:
        choice = main_menu()
        
        if choice == "1":
            binary = input("Enter a binary number: ")
            result = binary_to_denary(binary)
            print(f"The denary value is: {result}" if not isinstance(result, str) else result)
        
        elif choice == "2":
            try:
                denary = int(input("Enter a denary number: "))
                result = denary_to_binary(denary)
                print(f"The binary value is: {result}" if not isinstance(result, str) else result)
            except ValueError:
                print("Error: Please enter a valid integer.")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the program
converter_program()
