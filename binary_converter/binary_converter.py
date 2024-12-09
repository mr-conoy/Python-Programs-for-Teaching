# Main Menu Function
def main_menu():
    print("Binary-Denary Converter")
    print("1. Convert Binary to Denary")
    print("2. Convert Denary to Binary")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    return choice

# Binary to Denary Conversion
def binary_to_denary(binary_str):
    # Convert binary string to denary
    return int(binary_str, 2)

# Denary to Binary Conversion
def denary_to_binary(denary_int):
    # Convert denary integer to binary
    return bin(denary_int)[2:]

# Main Program
def converter_program():
    while True:
        choice = main_menu()
        
        if choice == "1":
            binary = input("Enter a binary number: ")
            denary = binary_to_denary(binary)
            print(f"The denary value is: {denary}")
        
        elif choice == "2":
            denary = int(input("Enter a denary number: "))
            binary = denary_to_binary(denary)
            print(f"The binary value is: {binary}")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the program
converter_program()
