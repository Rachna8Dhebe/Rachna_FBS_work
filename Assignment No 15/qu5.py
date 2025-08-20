s = input("Enter a string: ")
words = s.split()
small_words = [w for w in words if len(w) < 5]
print("Words less than 5 letters:", small_words)
