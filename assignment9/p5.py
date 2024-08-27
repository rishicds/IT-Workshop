def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Example usage
print(factorial(5))  # Output: 120
