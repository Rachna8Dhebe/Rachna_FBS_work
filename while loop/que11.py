n = int(input("Enter number: "))
temp = n
sum = 0

def factorial(x):
    f = 1
    i = 1
    while i <= x:
        f *= i
        i += 1
    return f

while temp > 0:
    digit = temp % 10
    sum += factorial(digit)
    temp //= 10

if sum == n:
    print("Strong Number")
else:
    print("Not a Strong Number")
