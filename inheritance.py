class person:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print("Name:", self.name)
class Student(person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
    def display_department(self):
        print("Department:", self.department)
student1 = Student("Priya", "AIML")
student1.display_name()
student1.display_department()
