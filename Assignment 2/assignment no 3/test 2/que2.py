digit=int(input("Enter the digital number:"))

first=digit//100
second=(digit//10)%10
third=digit%10

if(first==2*second and first==2*third):
    print("Yes you have done it")

else:
    print("Please try next time")

