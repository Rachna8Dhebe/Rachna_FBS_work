i=5
for i in range(1,6):
    print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    k=j-1
    for j in range(1,i):
        print(k,end=" ")
        k-=1
print()
       