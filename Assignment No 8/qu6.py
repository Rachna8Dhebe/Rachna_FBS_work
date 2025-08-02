def fibo(num):

 a=0
 b=1

 for i in range(num):
   print(a,end=" ")
   a,b=b,a+b
 return 

num=int(input("Enter number:"))
print(fibo(num))
