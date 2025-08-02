def leapYear():
year=int(input("Enter the year:"))
if(year%4==0):
    return"It is a leap year"

if(year%100==0):
    return"It is not leap year"

if(year%400==0):
    return"It is a leap year"

else:
    return"It is not a leap year"