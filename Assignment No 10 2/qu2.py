a = [5, 2, 9]
b = [8, 1, 4]
merged = a + b

# Bubble sort
n = len(merged)
for i in range(n):
    for j in range(n - i - 1):
        if merged[j] > merged[j + 1]:
            merged[j], merged[j + 1] = merged[j + 1], merged[j]

print("Merged and Sorted List:", merged)
