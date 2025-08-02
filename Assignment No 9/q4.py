
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)


n = int(input("Enter value of n: "))
print("Sum of first", n, "numbers is:", sum_n(n))
