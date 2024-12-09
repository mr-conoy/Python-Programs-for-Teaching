# Task 4: Binary Logic Program (Student View)
bin1 = "10101"  # Example binary number 1
bin2 = "11001"  # Example binary number 2

# Convert binary to denary
denary1 = int(bin1, 2)
denary2 = int(bin2, 2)

# Perform AND operation
and_result = bin(denary1 & denary2)[2:]

# Perform OR operation
or_result = bin(denary1 | denary2)[2:]

# Print the results
print("AND result:", and_result)
print("OR result:", or_result)

# Combine results for unlock code
unlock_code = and_result + or_result
print("Unlock code:", unlock_code)

# Task 4: Binary Logic Program (Teacher View)
bin1 = "10101"  # Binary 21
bin2 = "11001"  # Binary 25

# Convert binary to denary
denary1 = int(bin1, 2)
denary2 = int(bin2, 2)

# Perform AND operation
and_result = bin(denary1 & denary2)[2:]  # Output: 10001

# Perform OR operation
or_result = bin(denary1 | denary2)[2:]  # Output: 11101

# Print the results
print("AND result:", and_result)  # Output: 10001
print("OR result:", or_result)    # Output: 11101

# Combine results for unlock code
unlock_code = and_result + or_result
print("Unlock code:", unlock_code)  # Output: 1000111101
