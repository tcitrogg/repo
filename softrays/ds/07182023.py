import random
import math
from string import ascii_letters

import pyqrcode

# --- Recap: while loop

# i = 0

# while i < 5:
#     print(i)
#     i += 1


# --- Inbuilt Modules
basket = [ "apple", "banana", "pineapple", "mango", "carrot" ]

# Generate random floating point number between 0 and 1
# val = random.random()


# val = random.choice(basket)
# val = random.choice("radiance")

# val = math.e
# val = math.pi

# 5 * 4 * 3 * 2 * 1
# val = math.factorial(5)

# val = string.ascii_letters
# val = string.ascii_lowercase

# length = 7
# usrname = ""

# for i in range(length):
#     usrname += random.choice(ascii_letters)

# choices_list = random.choices(ascii_letters, k=length)
# usrname = "".join(choices_list)

# print(f"choices_list: {choices_list}")
# print(f"usrname: {usrname}")

qr = pyqrcode.create('Hello world!')
qr.svg('hello.svg')

# print(qr)