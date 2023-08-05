# ~ creating a function to read, write and append data to a file

def awr_file(filename, data="", mode="r", is_newline=True):
    """ t/bnierimi:
    Append, Write and Read `data` from a file
    modes:
        - a : Append `data` to a `file`
        - w : Write `data` to a `file`
        - r : Read `data` from a `file`
    """

    try:
        with open(filename, mode=mode) as of:
            if mode == "r":
                return of.read()
            elif mode in ["w", "a"]:
                if mode == "a" and is_newline:
                    data = f"\n{data}"
                of.write(data)
                return len(data)
            else:
                print(f"(x) Error : InvalidMode : {mode} is not a valid mode ")
    except Exception as error_message:
        print(f"(x) Error : {error_message.__class__.__name__} : {error_message}")


# ~ convert a string to dict
# x = eval(awr_file("my_data.txt"))
# print(type(x))

# fl = "todo.list"

# print(awr_file(fl, "- going to class", mode="w"))