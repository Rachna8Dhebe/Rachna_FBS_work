s = input("Enter a string: ")
vowels = "aeiouAEIOU"
no_vowels = "".join([ch for ch in s if ch not in vowels])
print("Without vowels:", no_vowels)
