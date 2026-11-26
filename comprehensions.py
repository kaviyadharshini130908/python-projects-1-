
numbers = [1, 2, 3, 4, 5]
squares = [number * number for number in numbers]
print("Numbers:", numbers)
print("Squares:", squares)
even_numbers = [number for number in numbers if number % 2 == 0]
print("Even numbers:", even_numbers)
students = ["Kaviya", "Priya", "Ravi"]
student_names = {
    name: len(name)
    for name in students
}
print("Student name lengths:", student_names)
