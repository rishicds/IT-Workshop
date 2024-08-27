def isPrime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

m,n=map(int,input().split())
for i in range(m,n+1):
    if isPrime(i)==True:
        print(i)