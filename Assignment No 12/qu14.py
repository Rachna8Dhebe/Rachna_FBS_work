s = "python is fun and python is easy"
words = s.split()   # (if split not allowed → manually split with loop)
count_dict = {}

for w in words:
    if w in count_dict:
        count_dict[w] += 1
    else:
        count_dict[w] = 1

print("Word occurrences:", count_dict)
