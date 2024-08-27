#wap in python to calculate gcd and lcm of two numbers

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    return (a*b)//gcd(a,b)

a,b=map(int,input().split())
print("gcd of",a,"and",b,"is",gcd(a,b))
print("lcm of",a,"and",b,"is",lcm(a,b))

'''
output:
12 15
gcd of 12 and 15 is 3
lcm of 12 and 15 is 60
'''