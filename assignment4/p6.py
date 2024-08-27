#WAP in python to calculate repetitive sum of the digits of the number until it becomes one digit

def repetitive_sum(n):
    if n < 10:
        return n
    else:
        sum = 0
        while n > 0:
            sum += n % 10
            n = n // 10
        return repetitive_sum(sum)

n = int(input("Enter a number: "))
print("Repetitive sum of the digits of the number is:", repetitive_sum(n))
