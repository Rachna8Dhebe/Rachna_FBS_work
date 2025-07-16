N=int(input("\nEnter N for power series: "))
sum=0
num=1

for i in range(1, N + 1):
    for j in range(i):  # calculate N^i
        num*= N
    sum+=num

print("Sum of power series is:", sum)
