
student = {
    "name": "Mythili",
    "age": 20,
    "department": "AIML"
}
print("Student details:")
print(student)
print("Name:", student["name"])
print("Age:", student.get("age"))
print("Student information:")
for key, value in student.items():
    print(key, ":", value)
student.update({"age": 21})
print("After update:")
print(student)
