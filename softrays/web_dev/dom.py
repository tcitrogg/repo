import os

from secaug import awr_file
from pyfiglet import Figlet

running = True
f = Figlet(font="slant")

print(f.renderText("> awr"))
print("The next gen file terminal program.")
print("└ Type `!help` to know how to use")

while running:
    cmd = input("\n<awr> ")
    if cmd.lower() in ["r", "read"]:
        fl = input("└ Enter file name: ")
        print(awr_file(fl))
    elif cmd.lower() in ["w", "write"]:
        fl = input("└ Enter file name: ")
        data = input("└ Enter data to write to file: ")
        awr_file(fl, data, "w")
    elif cmd.lower() in ["a", "add", "append"]:
        fl = input("└ Enter file name: ")
        data = input("└ Enter data to append to file: ")
        awr_file(fl, data, "a")
    elif cmd.lower() in ["rm", "remove"]:
        fl = input("└ Enter file name: ")
        os.remove(fl)

    elif cmd == "!help":
        print(""" (!) Help
    List of commands:
        - r  | read         : Read <data> from a <file>
        - w  | write        : Write <data> to a <file>
        - a  | add | append : Add <data> to a <file>
        - rm | remove       : Delete a <file>
        - help              : Show this dialog
        - exit              : Quit the program
    
                { your t/bnierimi }
""")
    elif cmd == "!exit":
        running = False
    else:
        print(f" (x) Error: Invalid command {cmd}")