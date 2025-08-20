s = "python"
n = 3  # remove index 3 (0-based)
new_str = ""

for i in range(len(s)):
    if i != n:
        new_str += s[i]

print("After removing:", new_str)
