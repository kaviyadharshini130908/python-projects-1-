
print("Numbers using for loop:")
for i in range(1, 6):
    print(i)
print("Numbers using while loop:")
number = 1
while number <= 5:
    print(number)
    number += 1
print("Using continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
print("Using break:")
for i in range(1, 6):
    if i == 4:
        break
    print(i)
