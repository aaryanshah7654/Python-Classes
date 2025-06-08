#sum of numbers
def sum_num(numbers):
    total=0
    for i in numbers:
        total += int(i)
    return total

print(sum_num("12345"))

#factorial of numbers
def factorial(num):
    total=1
    for i in range(1,num+1):
        total *= i
    return total

print(factorial(3))