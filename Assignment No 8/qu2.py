def sumOfOdd(num):
    sum=0
    for i in range(1,num+1):
        if(i%2!=0):
            sum+=i
    return sum
    
num=int(input("Enter number:"))
result=sumOfOdd(num)
print("Sum of all odd number from 1 to",num,"is:",result)
        