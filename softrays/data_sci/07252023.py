# ~ recap: lambda

add = lambda x: x + 2

# print(add(5))

# ~! Guess number game
from random import randint
# ~$ pip install pyfiglet
from pyfiglet import Figlet
# ~$ pip install colorama
from colorama import Fore, Back, init

f = Figlet(font="graffiti")

init(autoreset=True)

print(Fore.GREEN + f.renderText("{GNG}"))

answer = randint(0, 9)
chances = 3
g = 0

while g < chances:
    try:
        user_guess = int(input(f"{Fore.LIGHTMAGENTA_EX}[{chances - g}]{Fore.RESET} Guess the number: " + Fore.CYAN))
        print(Fore.RESET, end="")
        if user_guess == answer:
            print(Back.LIGHTGREEN_EX + Fore.BLACK + "(+) You are correct! :)")
            break
    except ValueError:
        print(Fore.RED + f"  └(x) Error: enter numbers only")
        g -= 1 # same as g = g - 1
    except Exception as error_message:
        print(Fore.RED + f"  └(x) Error: {error_message}")
        g -= 1
    g += 1 # same as g = g + 1
else:
    print(Back.RED + Fore.WHITE + "(x) Nah! you are wrong :(")

