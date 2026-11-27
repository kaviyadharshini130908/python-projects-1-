
def add(a: int, b: int) -> int:
    return a + b
def greet(name: str) -> str:
    return "Hello, " + name
def calculate_average(marks: list[int]) -> float:
    return sum(marks) / len(marks)
result = add(10, 20)
print("Sum:", result)
message = greet("Priya")
print(message)
marks = [80, 90, 85]
average = calculate_average(marks)
print("Average:", average)
