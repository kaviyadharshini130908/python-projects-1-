import csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Department", "Marks"])
    writer.writerow(["Priya", "AIML", 90])
    writer.writerow(["Ravi", "CSE", 85])
print("CSV file created successfully.")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    print("\nStudent Details:")
    for row in reader:
        print(row)
