p = float(input("Enter principal amount:"))
r = float(input("Enter annual nominal interest rate:"))
n = float(input("Enter number of times the interest is compounded per year:"))
t = float(input("Enter number of years:"))
print("What would become your money:", p*(1+(r/n))**n*t)
