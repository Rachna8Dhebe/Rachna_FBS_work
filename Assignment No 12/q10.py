s1 = "python"
s2 = "java"

len1 = 0
len2 = 0

for _ in s1:
    len1 += 1
for _ in s2:
    len2 += 1

if len1 > len2:
    print("Larger String:", s1)
elif len2 > len1:
    print("Larger String:", s2)
else:
    print("Both are equal")
