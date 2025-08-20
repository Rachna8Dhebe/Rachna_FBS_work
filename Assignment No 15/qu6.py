s = input("Enter a sentence: ")
words = s.split()
lengths = {w: len(w) for w in words}
print("Word lengths:", lengths)
