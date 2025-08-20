lst = [10, 25, 45, 33, 12]

# Bubble sort
n = len(lst)
for i in range(n):
    for j in range(n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("Second Largest:", lst[-2])
