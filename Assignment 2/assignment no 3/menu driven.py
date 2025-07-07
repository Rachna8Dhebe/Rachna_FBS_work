print("1.Area of rectangle")
print("2.Check whether given no is even or odd")
print("3.Find cube of given no.")

option=int(input("Enter option:"))

if(option ==1):
    length=int(input("Enter length:"))
    breadth=int(input("Enter breadth:"))
    area=length*breadth
    print("Area is:",area)

elif(option ==2):
    no=int(input("Enter number:"))
    if(no%2==0):
        print("Number is odd")
    else:
        print("Number is odd")
else:
    num=int(input("Enter the Number: "))
    ans=num**3
    print("Cube:",ans)