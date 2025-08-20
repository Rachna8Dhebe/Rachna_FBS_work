list = [3, 7, 1, 9, 4]
max_elem = list[0]
min_elem = list[0]

for i in list:
    if i > max_elem:
        max_elem = i
    if i < min_elem:
        min_elem = i

print("Maximum:", max_elem)
print("Minimum:", min_elem)
