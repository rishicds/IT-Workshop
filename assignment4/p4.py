# Function to convert binary to decimal
def binary_to_decimal(binary_num):
    decimal_num = 0
    binary_str = str(binary_num)
    for i in range(len(binary_str)):
        decimal_num += int(binary_str[i]) * (2 ** (len(binary_str) - i - 1))
    return decimal_num

# Input: binary number
binary_num = input("Enter a binary number: ")

# Convert and display the decimal equivalent
decimal_num = binary_to_decimal(binary_num)
print("Decimal equivalent:", decimal_num)
