file_name = "todo.txt"

# ~ recap
# # write to a file
# with open(file_name, "w") as opndfl:
#     opndfl.write("- renaming a file")

# # read from a file
# with open(file_name, "r") as opndfl:
#     data = opndfl.read()
# print(data)

# # append to a file
# with open(file_name, "a") as opndfl:
#     opndfl.write("\n- deleting a file")


# ~ renaming a file
import os

new_file_name = "list.txt"

# os.rename(file_name, new_file_name)


# ~ deleting a file
# os.remove(new_file_name)

# from parent directory
# parfilename = "../file_to_del.txt"
# with open(parfilename, "r") as opndfl:
#     data = opndfl.read()

# print(data)

# os.remove(parfilename)

# ~ print out current working directory
# cwd = os.getcwd()


# ~ list files and dir in a dir
# path = ".."
# list_of_files = os.listdir(path)
# # print(list_of_files)

# os.chdir(path)
# print(os.getcwd())

# for each_file in list_of_files:
#     if os.path.isfile(f"{each_file}"):
#         print(f"[file]: {each_file}")
#     else:
#         print(f"/dir /: {each_file}")

# |: ~ sort out files and dir

# for each_file in list_of_files:
    # if 


# ~ dict to & from a file
# 1.
my_data = {
    "name": "Radiance Be",
    "age": 1,
    "level": "demigod",
    "fav_food": "groceries"
}
file_name = "my_data.txt"

# 2.
with open(file_name, "w") as opndfl:
    opndfl.write(str(my_data))

# 3.
with open(file_name) as opndfl:
    x = opndfl.read()

print(type(x))

# 4.
# ?