# ~ make our app read multiple params
running = False
while running:
    cmd = input("[cmd]: ")
    if cmd == "exit":
        running = False
    elif cmd.startswith("w ") or cmd == "w":
        if len(cmd) == 1:
            filename = input("file: ")
        else:
            filename = cmd[2:]
        data = input("data: ")
        print(f"Writing | {data} to `{filename}`")
    elif cmd.startswith("r ") or cmd == "r":
        if len(cmd) == 1:
            filename = input("file: ")
        else:
            filename = cmd[2:]
        print(f"Reading | `{filename}`")
    else:
        print("(x) Error: invaild command")


# ~ exercises
# 1. Using Python as a calculator to solve engineering problems
#   - Factorial
number = 5
# result = 1
#     - @using while loop
# i = 0
# while i < number:
#     result *= number - i
#     i += 1

#     - @using for loop
# for i in range(number):
#     result *= number - i

#     - @using math
import math
result = math.factorial(number)
# print(result)

#     - @using recursion
# def factorial(number):
#     if number == 1:
#         return 1
#     else:
#         x = number * factorial(number - 1)
#         return x
# print(factorial(number))


#   - Circumference of a circle, radius
r = number
result = 2 * math.pi * r
# print(result)
