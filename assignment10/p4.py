def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_up_to(n):
    primes = {i for i in range(2, n + 1) if is_prime(i)}
    return primes


n = 20
prime_set = prime_numbers_up_to(n)
print("Prime numbers up to", n, ":", prime_set)
