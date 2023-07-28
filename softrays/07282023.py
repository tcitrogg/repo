# finally clause in try:except statement
# x = 3
# try:
#     12 / 0
# except Exception as error_message:
#     exception_name = error_message.__class__.__name__
#     print(f"(x) Error : {exception_name} : {error_message}")
# else:
#     print("the end")
# finally:
#     print("------------------")


# handling files
# r: read
# opened_file = open("list.txt")
# data = opened_file.read()
# opened_file.close()
# print(data)

# op_file = open("Docs/roadmap.txt", "r")
# data = op_file.read()
# op_file.close()
# print(data)

# op_file = open("/home/kgyk/Documents/README.nt", "r")
# data = op_file.read()
# op_file.close()
# print(data)

# w: write
# opened_file = open("list.txt", "w")
# opened_file.write("floating berries")
# opened_file.close()

# a: append
file_name = "list.txt"
# data_to_write = "\ngroceries"

opened_file = open(file_name, "a")
# opened_file.write(data_to_write)
# opened_file.close()


# ~ with
# with open(file_name, "r") as opened_file:
#     data = opened_file.read()


# print(data)

# with open("Birthday.txt", "wb") as opened_file:
#     opened_file.write(b"Happy Birthday to You!!! :)")

# with open("Birthday.txt", "rb") as opened_file:
#     data = opened_file.read()

# print(data.replace(b"roses", b"Roses"))