# ~ recap: Lambda

# add = lambda x: x + 2
# add = lambda x, y: x + y
# add = lambda *x: sum(x)

# print(add(3, 5, 10))


# ~ activity: Guess number game
from random import randint
from pyfiglet import Figlet
# pip install pyfiglet==0.7
from colorama import init, Fore
# pip install colorama

f = Figlet(font="slant")
init(autoreset=True)

print(Fore.RED + f.renderText("~~ GNG ~~"))
print("~~ Guess Number Game ~~")

correct_number = randint(0, 9)
chances = 3

for i in range(chances):
    no_chances = Fore.BLUE + f"{chances - i}" + Fore.RESET
    try:
        answer = int(input(f"[{no_chances}] Guess a number: " + Fore.CYAN))
        print(Fore.RESET, end="")
        if answer == correct_number:
            print(Fore.GREEN + "(+) Yeah! correct! :)" + Fore.RESET)
            break
    except ValueError:
        print(Fore.RED + f"  (x) Error : enter number only" + Fore.RESET)
    except Exception as error_message:
        print(Fore.RED + f"  (x) Error : {error_message}" + Fore.RESET)
else:
    print("(x) Nah! all wrong :(")
