lst = ["apple", "hi", "banana", "go"]

# Bubble sort by length
n = len(lst)
for i in range(n):
    for j in range(n - i - 1):
        if len(lst[j]) > len(lst[j + 1]):
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("Sorted by length:", lst)
