x=int(input("Enter a number: "))
copy=x
revnum=0
while x>0:
    revnum=revnum*10+x%10
    x=x//10
    
print(" "+str(copy))
print(-revnum)
print("------")
print(copy-revnum)