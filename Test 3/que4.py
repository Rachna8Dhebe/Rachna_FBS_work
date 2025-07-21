

rows = 5

for i in range(rows):
    for j in range(5):
        if i % 2 == 0:
            print((j + 1) % 2, end="")  
        else:
            print(j % 2, end="")        
    print()  
