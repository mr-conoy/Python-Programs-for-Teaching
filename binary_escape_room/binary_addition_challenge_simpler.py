# Task 2: Binary Addition Program (Student View)
bin1 = "1010"  # Example binary number 1
bin2 = "110"   # Example binary number 2

# Convert binary to denary
denary1 = int(bin1, 2)
denary2 = int(bin2, 2)

# Add the two numbers
result = denary1 + denary2

# Print the result
print("The result in binary is:", bin(result)[2:])

# Task 2: Binary Addition Program (Teacher View)
bin1 = "1010"  # Binary 10
bin2 = "110"   # Binary 6

# Convert binary to denary
denary1 = int(bin1, 2)
denary2 = int(bin2, 2)

# Add the two numbers
result = denary1 + denary2

# Print the result
print("The result in binary is:", bin(result)[2:])  # Output: 10000
