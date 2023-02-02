year=float(input("enter a year :"))
if(year<=0):
    print("invalid")
    year=int(input("enter a proper year: "))
yearfloat=float(year)
if(year==yearfloat):
    print("its not a year!")    
    year=int(input("enter a  proper year:"))
if(year%400==0)and (year%100==0):
    print(year," is a leap year")
elif(year%4==0)and(year%100!=100):
    print(year," is a leap year")
else:
    print(year," is not  leap year")
