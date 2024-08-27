def factorial(num):
    factorialsum=1
    for i in range(1,num+1):
        factorialsum*=i
    return factorialsum

series_sum=0
series=[]
for i in range(1,int(input())+1):
    series_sum+=i/factorial(i)
    series.append(f"{i}/{i}!")
    
print(series_sum)
print(series)