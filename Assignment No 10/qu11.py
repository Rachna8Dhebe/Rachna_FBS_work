list = [10, 15, 30, 45, 60]
m = 3
n = 5
print("Numbers divisible by", m, "and", n, "are:")

for i in list:
    if i % m == 0 and i % n == 0:
        print(i)
