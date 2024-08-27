uppercase = lowercase = numbers = 0

while True:
    x = input("Enter a number or letter, * to quit: ")
    if x == "*":
        break
    elif x.isupper():
        uppercase += 1
    elif x.islower():
        lowercase += 1
    elif x.isdigit():
        numbers += 1

print(uppercase, lowercase, numbers)