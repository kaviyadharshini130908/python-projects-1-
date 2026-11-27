
class Student:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    def display(self):
        return "Name: " + self.name
    def __str__(self):
        return self.name + " - " + self.department
student1 = Student("Priya", "AIML")
print(student1.display())
print(student1)
