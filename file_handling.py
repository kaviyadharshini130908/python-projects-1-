
with open("student.txt", "w") as file:
    file.write("Name: Priya\n")
    file.write("Department: AIML\n")
    file.write("Year: III Year\n")
print("File written successfully.")
with open("student.txt", "r") as file:
    content = file.read()
print("\nStudent Details:")
print(content)
