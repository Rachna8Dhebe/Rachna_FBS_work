num=int(input("Enter the number:"))
x=int(input("Enetr the number:"))
n=int(input("Enter the number:"))
sum=0
for i in range(1,n+1):
    term=(x**i)/(2*i)-1
    if(i%2==0):
        sum==term
    else:
        sum+=term
print(sum)