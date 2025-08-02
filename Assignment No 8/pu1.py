def sumOfSeries(num):
    ans=0
    for i in range(1,num+1):
        ans=ans+i
    return ans
    
def factorial(num):
    sum_fact=0
    fact=1

    for i in range(1,num+1):
        fact*=i
        sum_fact+=fact
    return sum_fact

def Exponential(num):
    sum=0
    for i in range(1,num+1):
        ans=num**i
        sum+=ans
    return sum
ch=0
while(ch!=4):
    print("1.Calling first function:")
    print("2.Calling second function:")
    print("3.Calling third function:")
    print("4.Exit")
    ch=int(input("Enter choice:"))

if(ch==1):
    num=int(input("Enter number:"))
    print(sumOfSeries(num))

elif(ch==2):
    num=int(input("Enter number:"))
    print(factorial(num))

elif(ch==3):
    num=int(input("Enter number:"))
    print(Exponential(num))

else:
    print("Exit")






