#reverse an integer
def reverse_num(number):
    if number < 0:
        return -int(str(-number)[::-1])
    else:
        return int(str(number)[::-1])
print(reverse_num(-123))

#Area of rectangle
def area_rectangle(height, width):
    if height > 0 and width > 0:
        return height * width
    else:
        return "height and width must be greater than 0"
print(area_rectangle(5,5))

#encrypted by ceaser chiper
def ceaser_chiper(code, step):
    Encrypted = ""
    for char in code:
        if char.isdigit():
            new_digit = (int(char) + step ) % 10
            Encrypted += str(new_digit)
        else:
            Encrypted += char
    return Encrypted
print(ceaser_chiper("1789", 4))    #numbers mah step 4 hunxa alphabet mah step 3