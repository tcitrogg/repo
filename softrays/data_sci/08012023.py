import os

# ~ recap
file_name = "todo.txt"

# with open(file_name, "w") as opndfl:
    # opndfl.write("- reading a file with python")

# with open(file_name, "r") as opndfl:
    # data = opndfl.read()
# print(data)

# with open(file_name, "a") as opndfl:
#     data = opndfl.write("\n- deleting a file with python")

# ~ renaming a file
# os.rename("hello.svg", "sun.svg")

# ~ delete a file
# os.remove("todo.txt")
# os.remove("main/readme.txt")

# ~ get current working directory
current_dir = os.getcwd()
# print(current_dir)

# ~ list a dir
path = "."
path = "/home/kgyk/Documents"
# path = "/home/kgyk/Documents/hawesome"

# list_of_files = os.listdir(path)

# print(list_of_files)
# for each_item in list_of_files:
#     if os.path.isdir(f"{path}/{each_item}"):
#         print(f"[file]: {each_item}")
#     else:
#         print(f"[dir ]: {each_item}")


# ~ dict to & from a file
# 1.
bio = {
    "first_name": "Radiance",
    "last_name": "Be",
    "age": 2
}
file_name = "secrets.dict"

# 2.
# with open(file_name, "w") as of:
#     of.write(str(bio))

# 3.
with open(file_name) as of:
    x = of.read()

# 4.
x = eval(x)
print(type(x))
# print(x["first_name"])