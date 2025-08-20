str1 = "listen"
str2 = "silent"

# Check length first
if len(str1) != len(str2):
    print("Not Anagrams")
else:
    # Convert to list and sort manually
    list1 = list(str1)
    list2 = list(str2)

    for i in range(len(list1)):
        for j in range(len(list1)-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]

    for i in range(len(list2)):
        for j in range(len(list2)-i-1):
            if list2[j] > list2[j+1]:
                list2[j], list2[j+1] = list2[j+1], list2[j]

    if list1 == list2:
        print("Strings are Anagrams")
    else:
        print("Not Anagrams")
