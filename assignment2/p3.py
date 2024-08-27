year=int(input("Enter a year "))
print(f"{year} is a leap year" if (year%4==0 and year%100!=0) or year%400==0 else f"{year} is not a leap year") 