list = [3, 7, 1, 9, 3, 4, 3]
num = int(input("Enter number to check: "))
found = False
count = 0

for i in list:
    if i == num:
        found = True
        count += 1

if found:
    print(num, "is present", count, "times.")
else:
    print(num, "is not in the list.")
