n=int(input("Enter a number:"))

a=1
b=0

for i in range(1,n+1):
    c=a+b
    print(c)
    a=b
    b=c