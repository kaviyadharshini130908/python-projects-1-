
students = [
    {"name": "mythili", "mark": 85},
    {"name": "Priya", "mark": 90},
    {"name": "Ravi", "mark": 78}
]
print("Student Details:")
for student in students:
    print("Name:", student["name"])
    print("Mark:", student["mark"])
    print()
students.append({"name": "Arun", "mark": 88})
print("After adding a student:")
for student in students:
    print(student)
