
def armstrong_sum(num, power):
    if num == 0:
        return 0
    digit = num % 10
    return digit ** power + armstrong_sum(num // 10, power)

def is_armstrong(num):
    power = len(str(num))
    return num == armstrong_sum(num, power)

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
