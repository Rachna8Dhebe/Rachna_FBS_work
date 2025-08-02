def Prime(num):
 sum=0

 for num in range(2,num+1):
    
    for i in range(2,num):
     if(num%i==0):
          break
     else:
          sum+=num

 return sum

num=int(input("Enter number:"))
result=Prime(num)
print("Sum of all prime number from 1 to",num,"is:",result)
        




    