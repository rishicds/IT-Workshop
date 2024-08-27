def create_square_dict(n):
    square_dict = {}
    for i in range(1, n+1):
        square_dict[i] = i * i
    return square_dict

# Example usage
n = 5
print(create_square_dict(n))
