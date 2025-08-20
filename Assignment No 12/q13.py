s = "Python1234"
letters = 0
digits = 0

for ch in s:
    if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        letters += 1
    elif ch >= '0' and ch <= '9':
        digits += 1

print("Letters:", letters)
print("Digits:", digits)
