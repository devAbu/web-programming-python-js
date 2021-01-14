import sys

x = int(input("x: "))
y = int(input("y: "))

result = x / y

print(f"{x} / {y} = {result}")

""" EXCEPTION """


x = int(input("x: "))
y = int(input("y: "))

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # Exit the program
    sys.exit(1)

print(f"{x} / {y} = {result}")
