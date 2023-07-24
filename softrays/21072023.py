# recap: creating functions

# def add(x, y):
#     # print(x + y)
#     if x > 10:
#         print("(x) Error: `x` is greater than 10")
#     else:
#         return x + y
#     print("the end")

# val = add(37, 50)
# print(val)


# lambda:
fx = lambda x: x + 3

# print(fx(5))

# add = lambda x, y: x + y
add = lambda x, y: x + y

# print(add(3, 50))

# print(add(4, add(9, add(4, 8))))

# def add(x, y):
#     return x + y

# value = add(3, 5)
# print(value)

def add(*x: tuple):
    val = sum(list(x))
    return val

# value = add(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(value)

# print("Radiance", add(4, 5), "Softrays", sep="~")

# def cube(**kvargs):
#     for each_key, each_val in kvargs.items():
#         print(f"{each_key}: {each_val}")

# cube(x=5, y=6, z=28, t="2023/07/21")


cube = lambda x: x**3

print(cube(10))