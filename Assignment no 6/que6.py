l=1
for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    l=j+1
    for j in range(1,i):
        print(l,end=" ")
        l+=1
    print()
    

