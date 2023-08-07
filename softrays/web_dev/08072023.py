# + Syntax in Python
# ~ multiple assignment
x = 2
x = t = 3
x = y = z = 5
# print(z)


# ~ unpacking to multiple variables
def leave():
    return "Radiance", 12, "Purple"

# print(leave())
name, age, color = leave()
# print(name)
# print(age)
# print(color)

item1, item2 = ["murasaki", "Gojo"]
# print(item1)
# print(item2)

# ~ make our app read multiple params
def cmd_check(cmd):
    splited_cmd = cmd.split()
    if len(splited_cmd) > 1:
        filename = cmd[2:]
    else:
        filename = input("[ Filename: ")
    return filename

running = False
while running:
    cmd = input("<[cmd] ")

    if cmd == "exit":
        running = False
    elif cmd.startswith("w"):
        filename = cmd_check(cmd)
        data = input("[ Data: ")
        print(f"Writing: *{data}* -> `{filename}`")
    elif cmd.startswith("r"):
        filename = cmd_check(cmd)
        print(f"Reading: `{filename}`")
    else:
        print("(x) Error: invaild command :", cmd)


# ~ exercises
# 1. Using Python as a calculator to solve engineering problems
#   - Factorial
number = 100
result = 1
#     - @using while loop
# i = 0
# while i < number:
#     result *= number - i
#     i += 1

#     - @using for loop
# for i in range(number):
#     result *= number - i

#     - @using math
# import math
from math import factorial, pi
result = factorial(100)
# print(result)

#     - (%) Pending: @using list
# result = []

#   - Circumference of a circle, radius
r = 5
result = 2 * pi * r
# print(result)



# spend 4 hours and become a Don

# ~ json

