# ~ recap: Lambda

# add = lambda x: x + 2
# add = lambda x, y: x + y
# add = lambda *x: sum(x)

# print(add(3, 5, 10))


# ~ activity: Guess number game
from random import randint
from pyfiglet import Figlet

f = Figlet(font="slant")

print(f.renderText("~~ GNG ~~"))
print("~~ Guess Number Game ~~")

correct_number = randint(0, 9)
chances = 5

for i in range(chances):
    try:
        answer = int(input(f"[{chances - i}] Guess a number: "))
        if answer == correct_number:
            print("(+) Yeah! correct! :)")
            break
    except ValueError:
        print(f"  (x) Error : enter number only")
    except Exception as error_message:
        print(f"  (x) Error : {error_message}")
else:
    print("(x) Nah! all wrong :(")
