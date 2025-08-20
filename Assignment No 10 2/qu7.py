a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
intersection = []

for i in a:
    for j in b:
        if i == j:
            found = False
            for k in intersection:
                if k == i:
                    found = True
                    break
            if not found:
                intersection.append(i)

print("Intersection:", intersection)
