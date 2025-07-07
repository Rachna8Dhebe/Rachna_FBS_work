year=int(input("Enter the year:"))
if(year%4==0):
    print("It is a leap year")

if(year%100==0):
    print("It is not leap year")

if(year%400==0):
    print("It is a leap year")

else:
    print("It is not a leap year")