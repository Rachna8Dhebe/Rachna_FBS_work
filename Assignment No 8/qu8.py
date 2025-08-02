def Reverse(num):
    reverse=0
    while(num>0):
        a=num%10
        num=num//10
        reverse=(reverse*10)+a
    return reverse

num=int(input("Enter number:"))
print(Reverse(num))