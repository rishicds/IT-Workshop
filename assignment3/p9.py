sum_series=0
series=[]
term=1
for i in range(1,int(input())):
    sum_series+=term
    term=term*2
    series.append(f"{term}")
    
print(sum_series)
print(series)