num=int(input())
digits=len(str(num))
copy=num
armstrongno=0
while(num!=0):
    last_digit=num%10
    armstrongno+=last_digit**digits
    num//=10
if(armstrongno==copy):
    print("It is armstrong")
    