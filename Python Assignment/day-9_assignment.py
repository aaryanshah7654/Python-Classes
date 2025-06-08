#Class Assignment

#1 Student Gradebook using lists and dictionaries.
students = [
    {"name": "Alice", "grades": [90, 85, 88]},
    {"name": "Bob", "grades": [70, 75, 80]},
    {"name": "Charlie", "grades": [95, 92, 90]},
]

for student in students:
    grades = student["grades"]
    avg = sum(grades) / len(grades)
    student["average"] = avg  

students_sorted = sorted(students, key=lambda x: x["average"], reverse=True)

for student in students_sorted:
    print(f"{student['name']} - Grades: {student['grades']} - Average: {student['average']:.2f}")

#2 Word Counter
def word_counter(data):
    if isinstance(data, str):
        words = data.split()  
    elif isinstance(data, list):
        words = data
    else:
        return "Invalid input"

    return len(words)
print(word_counter("my name is aaryan shah"))