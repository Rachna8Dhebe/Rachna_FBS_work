num=int(input("Enter number:"))
temp=num
count=0
while(num!=0):
    num=num//10
    count+=1
num=temp
sum=0
while(num!=0):
    a=num%10
    num=num//10
    sum=sum+(a**count)
if(sum==temp):
    print("It is a armstrom:")
else:
    print("It is not armstrom:")

