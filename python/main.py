""" INTRODUCTION """
print("Hello, world!")

""" VARIABLES """
a = 28
b = 1.5
c = "Hello!"
d = True
e = None

""" INPUT """
name = input("Your name please: ")
print("Hello, " + name)

""" STRING FORMAT """
print(f"Hello, {input('Name: ')}")

""" CONDITIONS """
num = int(input("Number: "))
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is 0")

""" Strings """
name = "Harry"
print(name[0])  # H
print(name[1])  # a
""" name[0] = "A" # ERROR """

""" LISTS """
# This is a Python comment
names = ["Harry", "Ron", "Hermione"]
# Print the entire list:
print(names)
# Print the second element of the list:
print(names[1])
# Add a new name to the list:
names.append("Draco")
# Print the new list:
print(names)
# Sort the list:
names.sort()
# Print the sorted list:
print(names)

""" TUPLES """

point = (12.5, 10.6)
# the entrie tuple
print(point)
# the second element
print(point[1])

""" SETS """
# Create an empty set:
s = set()

# Add some elements:
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.add(1)

# Remove 2 from the set
s.remove(2)

# Print the set:
print(s)

# Find the size of the set:
print(f"The set has {len(s)} elements.")

""" DICTIONARIES """
# Define a dictionary
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
# Print out Harry's house
print(houses["Harry"])
# Adding values to a dictionary:
houses["Hermione"] = "test"
# Print out Hermione's House:
print(houses["Hermione"])

""" LOOPS """

for i in [0, 1, 2, 3, 4, 5]:
    print(i)

for i in range(6):
    print(i)

# Create a list:
names = ["Harry", "Ron", "Hermione"]

# Print each name:
for name in names:
    print(name)

name = "Harry"
for char in name:
    print(char)

""" FUNCTIONS """


def square(x):
    return x * x


for i in range(10):
    print(f"The square of {i} is {square(i)}")


""" MODULES """
