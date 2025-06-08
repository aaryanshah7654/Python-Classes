from datetime import datetime

birthdate_str = input("Enter your Birthdate (YYYY-MM-DD):")

birthdate = datetime.strptime(birthdate_str,"%Y-%m-%d")

today = datetime.today()

age = today.year - birthdate.year

if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

print(f"Your age is: {age}")