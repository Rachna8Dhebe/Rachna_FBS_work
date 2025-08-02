def sumOfDigits(num):
   sum=0

   while(num!=0):
    a=num%10
    num=num//10
    sum=sum+a
   return sum

num=int(input("Enter number:"))
print(sumOfDigits(num))




