
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)


def reverse_number(n, digits=None):
    if digits is None:
        digits = count_digits(n) - 1
    if n == 0:
        return 0
    return (n % 10) * (10 ** digits) + reverse_number(n // 10, digits - 1)

num = int(input("Enter a number to reverse: "))
print("Reversed number:", reverse_number(num))
