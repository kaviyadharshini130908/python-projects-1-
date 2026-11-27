try:
    number = int(input("Enter a number: "))
    print("Number:", number)
except ValueError:
    print("Please enter a valid number.")
finally:
    print("ValueError example completed.")
student = {"name": "Kaviya", "department": "AIML"}
try:
    print("Marks:", student["marks"])
except KeyError:
    print("Marks key is not available.")
finally:
    print("KeyError example completed.")
try:
    file = open("missing.txt", "r")
    file.close()
except FileNotFoundError:
    print("File not found.")
finally:
    print("File example completed.")
