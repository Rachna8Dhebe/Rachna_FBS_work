s = "hello world python"
new_str = ""

for ch in s:
    if ch == " ":
        new_str += "-"
    else:
        new_str += ch

print("New String:", new_str)
