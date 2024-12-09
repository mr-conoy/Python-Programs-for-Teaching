# Binary Addition Program (Student View)
def binary_addition(bin1, bin2):
    # Convert binary to denary
    denary1 = int(bin1, 2)
    denary2 = int(bin2, 2)
    
    # Perform addition
    result_denary = denary1 + denary2

    # Convert result back to binary
    result_binary = bin(result_denary)[2:]  # [2:] removes '0b' prefix
    return result_binary

# Input two binary numbers
bin1 = "1010"  # Example binary number 1
bin2 = "110"   # Example binary number 2

# Complete the following line to call the function:
# print(binary_addition(___, ___))

# Binary Addition Program (Teacher View, Solution)
def binary_addition(bin1, bin2):
    # Convert binary to denary
    denary1 = int(bin1, 2)
    denary2 = int(bin2, 2)
    
    # Perform addition
    result_denary = denary1 + denary2

    # Convert result back to binary
    result_binary = bin(result_denary)[2:]  # [2:] removes '0b' prefix
    return result_binary

# Input two binary numbers
bin1 = "1010"  # Example binary number 1
bin2 = "110"   # Example binary number 2

# Complete the following line to call the function:
print(binary_addition(bin1, bin2))  # Output: 10000
