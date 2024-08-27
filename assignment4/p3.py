# Function to convert decimal to binary
def decimal_to_binary(decimal_num):
    if decimal_num >= 1:
        decimal_to_binary(decimal_num // 2)
    print(decimal_num % 2, end='')

# Input: decimal number
decimal_num = int(input("Enter a decimal number: "))

print("Binary equivalent: ", end='')
if decimal_num == 0:
    print(0)
else:
    decimal_to_binary(decimal_num)
