lst = [1, 2, 3, 4, 5, 6, 7]
result = []

for i in lst:
    if i % 2 != 0:
        result.append(i)

print("List after removing even numbers:", result)
