# Binary Logic Challenge (Student View)
def binary_logic(bin1, bin2):
    # Convert binary to denary
    denary1 = int(bin1, 2)
    denary2 = int(bin2, 2)
    
    # Apply AND and OR operations
    and_result = denary1 & denary2
    or_result = denary1 | denary2
    
    # Convert results back to binary
    return bin(and_result)[2:], bin(or_result)[2:]

# Input two binary numbers
bin1 = "10101"  # Example binary number 1
bin2 = "11001"  # Example binary number 2

# Complete the following line to call the function:
# print(binary_logic(___, ___))

# Binary Logic Challenge (Teacher View, Solution)
def binary_logic(bin1, bin2):
    # Convert binary to denary
    denary1 = int(bin1, 2)
    denary2 = int(bin2, 2)
    
    # Apply AND and OR operations
    and_result = denary1 & denary2
    or_result = denary1 | denary2
    
    # Convert results back to binary
    return bin(and_result)[2:], bin(or_result)[2:]

# Input two binary numbers
bin1 = "10101"  # Example binary number 1
bin2 = "11001"  # Example binary number 2

# Print the result
print(binary_logic(bin1, bin2))  # Output: ('10001', '11101') => Combine: 1000111101
