def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
start=int(input("Enter number:"))
stop=int(input("Enter the number:"))
print("Factorial of given range:{start},{stop}")
for i in range(start,stop+1):
 print("f{i}!=factorial(i)")

