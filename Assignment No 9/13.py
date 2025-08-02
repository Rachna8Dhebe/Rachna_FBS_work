def reverse(num,rev):
    if (num!=0):
        a=num%10
        rev=rev*10+a
        reverse(num//10,rev)
    else:
        num=int
        ans=reverse(num,0)