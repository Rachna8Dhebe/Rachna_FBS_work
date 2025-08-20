lst = [3, 7, 3, 1, 3, 9, 4]
num = int(input("Enter element to remove: "))
new_lst = []

for i in lst:
    if i != num:
        new_lst.append(i)

print("List after removal:", new_lst)
