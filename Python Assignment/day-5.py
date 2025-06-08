#number is armstrong or not
def armstrong(number):
    digits= str(number)
    total = 0
    for digit in digits:
        total += int(digit) ** 3
    return total == number
print(armstrong(153))

# for area of rectangle
def area_rectangle(height, width):
    if height > 0 and width > 0:
        return height * width
    else:
        return "height and width > 0"
print(area_rectangle(5,5))

#for volume of rectangle
def volume_rectangle(length, width, height):
    if length > 0 and width > 0 and height > 0:
        return length * width * height
    else:
        return "number should be > 0"
print(volume_rectangle(5,5,5))

#remove the vowels from string
def remove_vowels(string):
    vowels = "aeiouAEIOU"
    final_string = ""
    for char in string:
        if char not in vowels:
            final_string += char
    return final_string
print(remove_vowels("apple"))

#reverse an integer
def reverse_int(digit):
    if digit < 0:
        return -int(str(-digit)[::-1])
    else:
        return int(str(digit)[::-1])
print(reverse_int(-123))

#factorial of numbers
def factorial(num):
    total=1
    for i in range(1,num+1):
        total *= i
    return total
print(factorial(5))

#factorial of number using recursive function
def factorial_recursive(num):
    if num == 0 or num == 1:     #base case
        return 1
    else:
        return num * factorial(num-1)    #recursive case
print(factorial_recursive(5))