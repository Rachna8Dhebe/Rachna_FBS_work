n = int(input("Enter the value of N: "))
sum = 0
fact = 1

for i in range(1, n + 1):
    fact *= i       
    sum += i / fact 

print("Sum of the series is:", sum)
