# Task 3: Binary Multiplication Program (Student View)
bin1 = "101"   # Example binary number 1
bin2 = "11"    # Example binary number 2

# Convert binary to denary
denary1 = int(bin1, 2)
denary2 = int(bin2, 2)

# Multiply the two numbers
result = denary1 * denary2

# Print the result
print("The result in binary is:", bin(result)[2:])

# Task 3: Binary Multiplication Program (Teacher View)
bin1 = "101"   # Binary 5
bin2 = "11"    # Binary 3

# Convert binary to denary
denary1 = int(bin1, 2)
denary2 = int(bin2, 2)

# Multiply the two numbers
result = denary1 * denary2

# Print the result
print("The result in binary is:", bin(result)[2:])  # Output: 1111
