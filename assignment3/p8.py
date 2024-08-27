
sum_series=0
series=[]
for i in range(1,x:=int(input())+1):
    sum_series+=i**2/i
    series.append(f"{i**2}/{i}")
    
print(sum_series)
print(series)