for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    l=k-1
    for k in range(1,i):
        print("*",end=" ")
        k-=1
    print()