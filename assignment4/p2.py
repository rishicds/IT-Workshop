possum=negsum=posavg=negavg=poscount=negcount=0
while(True):
    x=int(input("Enter a number,-1 to exit "))
    if(x==-1):
        break
    elif(x>=0):
        possum+=x
        poscount+=1
    else:
        negsum+=x
        negcount+=1
        
posavg=possum/poscount
negavg=negsum/negcount
#print(possum,poscount,posavg)
#print(negsum,negcount,negavg)
print(f"Average of positive numbers is {posavg} and negative numbers is {negavg}")   