# Merge Two Dictionaries:
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3}
merged = {**dict1, **dict2} 
print(merged)

# Invert a Dictionary 
my_dict = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in my_dict.items()}
print(inverted)

#Nested Dictionary: Store student grades in subjects
students_grades = {
    "Aaryan": {"Math": 90,
              "Science": 85,
              "English": 88 },
    "person_1": {"Math": 75,
            "Science": 80,
            "English": 70 },
    "person_2": {"Math": 85,
                "Science": 92,
                "English": 95 },
}
print(students_grades["Aaryan"]["Math"]) 
print(students_grades["person_2"]["Science"]) 