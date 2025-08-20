list = [3, 7, 1, 9, 3, 4, 7]
unique = []

for i in list:
    duplicate = False
    for j in unique:
        if i == j:
            duplicate = True
            break
    if not duplicate:
        unique.append(i)

print("List without duplicates:", unique)
