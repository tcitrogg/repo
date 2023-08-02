# ~ creating a function to read, write and append data to a file

def rwa_file(file_name, data="...", is_newline=True, mode="r"):
    """ t/bnierimi:
      Read, Write and Append data to a file

      Usage:
        - `file_name`  : <string>  Name of file to change or work with.
        - `data`       : <string>  Data to write or append to `file_name`
        - `is_newline` : <boolean> Start appending `data` on a newline
        - `mode`       : <string>  <r, w, a>
           - `r`       : Read
           - `w`       : Write
           - `a`       : Append
    """
    # First method:
    if mode == "r":
        with open(file_name) as of:
            return of.read()
    elif mode == "w":
        with open(file_name, mode=mode) as of:
            of.write(data)
        return len(data)
    elif mode == "a":
        with open(file_name, mode=mode) as of:
            if is_newline:
                data = f'\n{data}'
            of.write(data)
        return len(data)

            # # ! The code below will do the same thing as the if statement above
            # of.write(f'\n{data}' if is_newline else data)
    else:
        print(f"(x) Error : InvalidMode : {mode} is not a valid mode ")

    # Second method:
    # try:
    #     with open(file_name, mode=mode) as of:
    #         if mode == "r":
    #             return of.read()
    #         elif mode == "w":
    #             of.write(data)
    #             return len(data)
    #         elif mode == "a":
    #             if is_newline:
    #                 data = f'\n{data}'
    #             of.write(data)
    #             return len(data)
    # except Exception as error_message:
    #     print(f"(x) Error : {error_message.__class__.__name__} : {error_message}")


fn = "secrets.dict"
secrets = """└[yours bnierimi]"""
# print(rwa_file(fn, data=secrets, mode="p"))
# help(rwa_file)