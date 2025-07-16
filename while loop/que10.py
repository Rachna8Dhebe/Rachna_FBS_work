n = int(input("Enter number: "))
i = 1
sum = 0
while i < n:
    if n % i == 0:
        sum += i
    i += 1
if sum == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
