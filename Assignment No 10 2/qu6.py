a = [1, 2, 3]
b = [3, 4, 5]
union = []

for i in a:
    union.append(i)

for i in b:
    found = False
    for j in union:
        if i == j:
            found = True
            break
    if not found:
        union.append(i)

print("Union:", union)
