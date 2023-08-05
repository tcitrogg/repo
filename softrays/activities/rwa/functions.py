import os
import json

RECORDS = "RECORDS.rwarec"

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
    else:
        print(f"(x) Error : InvalidMode : {mode} is not a valid mode ")

def initRecords():
    "Check if <file> exists"
    if not os.path.exists(RECORDS):
        json.dump({}, open(RECORDS, "w"), indent=2)

def readRecords():
    "Read records from <file>"
    return json.load(open(RECORDS))

def addToRecords(key, new_change):
    data = readRecords()
    if key not in data.keys():
        data[key] = []
    data[key].append(new_change)
    json.dump(data, open(RECORDS, "w"), indent=2)

def removeFromRecords(key):
    data = readRecords()
    if key not in data.keys() or len(data[key]) == 0:
        print("(x) Error: can't undo cause no change was recorded")
    else:
        list_of_changes = data[key]
        list_of_changes.pop()
        data[key] = list_of_changes
        json.dump(data, open(RECORDS, "w"), indent=2)
        if len(list_of_changes) > 1:
            return list_of_changes[-1]
        else:
            print("(x) Error: can't revert no more, no previous change")
