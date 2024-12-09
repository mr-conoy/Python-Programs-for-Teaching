# Binary Multiplication Program (with errors) (Student View)
def binary_multiply(bin1, bin2):
    denary1 = int(bin1, 2)
    denary2 = int(bin2, 2)
    
    # Perform multiplication (logical error: uses addition instead)
    result_denary = denary1 + denary2
    
    # Convert result back to binary
    return bin(result_denary)[2:]

bin1 = "101"
bin2 = "11"

# Print the result (syntax error here)
printbinary_multiply(bin1, bin2)


# Binary Multiplication Program (corrected) (Teacher View, Solution)
def binary_multiply(bin1, bin2):
    denary1 = int(bin1, 2)
    denary2 = int(bin2, 2)
    
    # Perform multiplication
    result_denary = denary1 * denary2
    
    # Convert result back to binary
    return bin(result_denary)[2:]

bin1 = "101"  # Example binary number 1 (5)
bin2 = "11"   # Example binary number 2 (3)

# Print the result
print(binary_multiply(bin1, bin2))  # Output: 1111

