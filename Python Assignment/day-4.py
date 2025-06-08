#reverse a string
def reverse(string):
    return string[::-1]   #[suru:end:step]

print(reverse("PYTHON"))

#print a pattern
def pattern():
    for i in range(1, 6):
        print("*" * i)

pattern()

#if a year is leap year or not
def leap_year(year):
    if year % 4 ==0:
        if year % 100 != 0 or year % 400 == 0:  
            return True
    return False

print(leap_year(2012))
print(leap_year(2017))

#print a 3rd index of string
def third_index(string):
    if len(string) > 3:
        return string[0:3]
    else:
        return ("")
print(third_index("Aaryan"))
print(third_index("Ant"))

#print number of vowels and consonants 
def vowels_and_consonant(string):
    vowels = "aeiouAEIOU"
    vowels_num = 0
    consonant_num = 0

    for i in string:
        if i in vowels:
            vowels_num += 1
        else:
            consonant_num +=1
    return vowels_num, consonant_num        
print(vowels_and_consonant("Python"))

#string is palindrome or not
def palindrome(string):
    string = string.replace(" ", "").lower() 
    if string == string[::-1]:
        return True
    else:
        return False
print(palindrome("racecar"))
print(palindrome("python"))
print(palindrome("121"))

#remove the string
def remove_string(string):
    return string.replace("yan", "")
print(remove_string("aaryan"))