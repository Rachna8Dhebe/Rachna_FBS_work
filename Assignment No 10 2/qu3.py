lst = [[1, 4], [3, 1], [5, 2]]

# Bubble sort by second element
n = len(lst)
for i in range(n):
    for j in range(n - i - 1):
        if lst[j][1] > lst[j + 1][1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("Sorted by second element:", lst)
