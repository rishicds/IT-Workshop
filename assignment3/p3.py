m,n=map(int,input().split())
for i in range(m,n+1):
    print(f"{i} is even" if i%2==0 else f"{i} is odd")