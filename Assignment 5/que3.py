num=int(input("Enter the number of passengers:"))
ticket=float(input("Enter the per ticket cost:"))
age=int(input("Enetr the age of passengers:"))
sum=0

for i in range(1,num+1):
    if age < 12:
        fare=ticket* 0.7
    elif age > 59:
        fare=ticket* 0.5
    else:
        fare=ticket
    sum+=fare
print("The total amount paid for all passengers:",sum)


    