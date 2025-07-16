start = int(input("Enter start: "))
end = int(input("Enter end: "))
i = start
while i <= end:
    if i % 7 == 0 and i % 5 == 0:
        i += 1
        print(i)
    
