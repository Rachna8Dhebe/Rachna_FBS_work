lst = [1, 2, 3, 4, 5, 6]
result = []

for i in lst:
    if i % 2 != 0:
        result.append(i)

print("After removing even numbers:", result)
