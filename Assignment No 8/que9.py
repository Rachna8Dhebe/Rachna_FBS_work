def Palindrom():
    num=int(input("Enter number:"))
    copy=num
    hun=num//100
    ten=(num//10)%10
    un=num%10
    reverse=un*100+ten*10+hun

    if (reverse==copy):
        return"t is a palindrome"
    else:
        return"It is not palindrome"
    
print(Palindrom())
       
    