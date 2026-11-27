import json
student = {
    "name": "Priya",
    "department": "AIML",
    "year": "II Year"
}
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
print("JSON data saved successfully.")
with open("student.json", "r") as file:
    data = json.load(file)
print("\nStudent Details:")
print(data)
print("Name:", data["name"])
print("Department:", data["department"])
