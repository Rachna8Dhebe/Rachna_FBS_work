n = int(input("Enter how many prime numbers to print: "))
count = 0
num = 2

print(f"First {n} prime numbers are:")

while count < n:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
        count += 1
    num += 1
