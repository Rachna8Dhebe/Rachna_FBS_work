n = 5 

for i in range(1, 6):
    print("  " * (6 - i), end="")

    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print(j, end="   ")
        else:
            print(" ", end="   ")

    print() 
