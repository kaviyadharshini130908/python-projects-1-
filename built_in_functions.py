
marks = [85, 90, 78, 95, 88]
print("Number of students:", len(marks))
print("Total marks:", sum(marks))
print("Lowest mark:", min(marks))
print("Highest mark:", max(marks))
print("Sorted marks:", sorted(marks))
print("Student marks with index:")
for index, mark in enumerate(marks, start=1):
    print(index, ":", mark)
names = ["Kaviya", "Priya", "Ravi"]
student_marks = [85, 90, 78]
print("Student names and marks:")
for name, mark in zip(names, student_marks):
    print(name, ":", mark)
