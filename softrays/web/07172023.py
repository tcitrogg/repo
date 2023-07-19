import random
import math
import os
from string import ascii_letters, digits
import platform
import pyttsx4

# recap while loop
# i = 0
# while i < 5:
#     print(i)
#     i += 1 

basket = [ "apple", "banana", "mango", "pineapple", "carrot" ]

# check out inbuilt modules{packages}

# ~ random
# Generate a random floating point number between the values:[0, 1]
# val = random.random()


# Pick a random item from the value given
# val = random.choice("radiance")

# Pick random item and return a list
# val = random.choices(basket)

# val = random.choice(digits)

# ~ string
# length = 7
# mixedChars = ascii_letters + digits
# usrname = ""

# for i in range(length):
#     usrname += random.choice(mixedChars)

# print(usrname)

# ~ math
piVal = math.pi
# print(math.floor(piVal))

# ~ os
# print(os.getcwd())

# ~ platform
# print(platform.architecture())

# ~ pyttsx4
engine = pyttsx4.init()
# engine.say('this is an english text to voice test.')
# engine.runAndWait()



# our own f(x)s
def pt():
    print("Yo! man's name is Me")
    print("The end")

# pt()

# def pt(text):
#     print(f"pt: {text}")

# pt("tatsumaki")


def pt(prompt, text=""):
    """(bnierimi):
    ### f(pt)
    Printing out a `prompt` like ChatGPT and a `text` as response"""
    print(f"{prompt}: {text}")

# pt(prompt="Jarvis", text="Yo! rest")
# pt("tatsumaki")

# my(Virtual Assistant)
def say(text, prompt="Alfred"):
    print(f"{prompt}: {text}")
    engine.say(text)
    engine.runAndWait()

name = input("Enter your name: ")
cmd = input(f"{name}: ")
say(cmd)