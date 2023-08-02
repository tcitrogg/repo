import os
from pyfiglet import Figlet
from augsec import rwa_file

f = Figlet(font="graffiti")
print(f.renderText("rwa"))
print("[rwa], the next gen file terminal operator")
print("└ Type, `help` for dialog on how to use.")

running = True

while running:
    try:
        cmd = input("\n┌[rwa] ")
        if cmd.lower() in ["r", "read"]:
            fl = input("└|Enter filename: ")
            if fl == ":exit":
                pass
            else:
                print(rwa_file(fl))

        elif cmd.lower() in ["w", "write"]:
            fl = input("| Enter filename: ")
            if fl == ":exit":
                pass
            else:
                data = input("└|Enter data to write to file: ")
                rwa_file(fl, data, mode="w")

        elif cmd.lower() in ["a", "add", "append"]:
            fl = input("| Enter filename: ")
            if fl == ":exit":
                pass
            else:
                data = input("└|Enter data to add to file: ")
                rwa_file(fl, data, mode="a")

        elif cmd.lower() in ["rm", "remove"]:
            fl = input("| Enter filename: ")
            if fl == ":exit":
                pass
            else:
                os.remove(fl)

        elif cmd == "help":
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

        elif cmd == "exit":
            break
        else:
            print("└(x) Error : Invalid command, use help")
    except Exception as error_message:
        print(f"└(x) Error : {error_message.__class__.__name__} : {error_message}")
