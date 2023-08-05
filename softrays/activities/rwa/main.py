import os
from pyfiglet import Figlet
# from activities.rwa.functions import rwa_file
import functions as fx

f = Figlet(font="graffiti")
print(f.renderText("rwa"))
print("[rwa], the next gen file terminal operator")
print("└ Type, `help` for dialog on how to use.")

running = True

while running:
    fx.initRecords()
    try:
        cmd = input("\n┌[rwa] ")
        if cmd.lower() in ["r", "read"]:
            fl = input("└|Enter filename: ")
            if fl == ":exit":
                pass
            else:
                print(fx.rwa_file(fl))

        elif cmd.lower() in ["w", "write"]:
            fl = input("| Enter filename: ")
            if fl == ":exit":
                pass
            else:
                data = input("└|Enter data to write to file: ")
                fx.rwa_file(fl, data, mode="w")
            fx.addToRecords(fl, data)

        elif cmd.lower() in ["a", "add", "append"]:
            fl = input("| Enter filename: ")
            if fl == ":exit":
                pass
            else:
                data = input("└|Enter data to add to file: ")
                fx.rwa_file(fl, data, mode="a")
            data = fx.rwa_file(fl)
            fx.addToRecords(fl, data)

        elif cmd.lower() in ["rm", "remove"]:
            fl = input("| Enter filename: ")
            if fl == ":exit":
                pass
            else:
                os.remove(fl)

        elif cmd.lower() in ["undo"]:
            fl = input("| Enter filename: ")
            data = fx.removeFromRecords(fl)
            if data != None:
                fx.rwa_file(fl, data, mode="w")

        elif cmd == "help":
            print(""" (!) Help
    List of commands:
        - r  | read         : Read <data> from a <file>
        - w  | write        : Write <data> to a <file>
        - a  | add | append : Add <data> to a <file>
        - rm | remove       : Delete a <file>
        - undo              : Undo changes made a <file>
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
