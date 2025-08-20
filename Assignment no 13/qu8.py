s = "python is fun and python is easy"
words = s.split()
freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print("Word Frequency:", freq)
