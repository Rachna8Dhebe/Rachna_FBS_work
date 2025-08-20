lst = [3,7, 1, 9, 4]
largest = second = -999999

for i in lst:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest element:", second)
