d1 = {1: "apple", 2: "banana"}
d2 = {3: "cherry", 4: "date"}

d3 = {}

# Copy d1
for k in d1:
    d3[k] = d1[k]

# Copy d2
for k in d2:
    d3[k] = d2[k]

print("Concatenated:", d3)
