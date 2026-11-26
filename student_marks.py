
def calculate_statistics(marks):
    if len(marks) == 0:
        return None
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    return average, highest, lowest
marks = [85, 90, 78, 95, 88]
result = calculate_statistics(marks)
if result is not None:
    average, highest, lowest = result
    print("Student Marks:", marks)
    print("Average Mark:", average)
    print("Highest Mark:", highest)
    print("Lowest Mark:", lowest)
else:
    print("No marks available.")
