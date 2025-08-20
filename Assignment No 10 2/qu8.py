rows = 10
cols = 10
num = 1

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(num)
        num += 1
    if i % 2 == 1:
        row.reverse()
    print(row)
