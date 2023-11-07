# SOFTRAYS_DICTIONARY = {
#     "apple": [
#         "A round shaped fruit with green or red skin",
#         "Expensive org."
#     ]
# }

# # print(SOFTRAYS_DICTIONARY)

# value_for_apple = SOFTRAYS_DICTIONARY["apple"]
# # print(value_for_apple)

# basket = ["apple", "mango", "orange", "pineapple"]

# # for each_item in basket:
# #     print(each_item)

# for k in SOFTRAYS_DICTIONARY:
#     if value_for_apple == SOFTRAYS_DICTIONARY[k]:
#         print(k)

# ----- 

# 2 specials chars
# 2 Uppercase letters
# 2 Lowercase letters
# 2 Numbers

import string
import random

no_of_uppercase_letters = int(input("Number of uppercase letters: "))
no_of_lowercase_letters = int(input("Number of lowercase letters: "))
no_of_punctuations = int(input("Number of punctuations: "))
no_of_digits = int(input("Number of digits: "))

all_passwords = []

for i in range(0, 10):
    pwd = []
    pwd += random.choices(string.ascii_uppercase, k=no_of_uppercase_letters)
    pwd += random.choices(string.ascii_lowercase, k=no_of_lowercase_letters)
    pwd += random.choices(string.punctuation, k=no_of_punctuations)
    pwd += random.choices(string.digits, k=no_of_digits)
    random.shuffle(pwd)
    # pwd = "".join(pwd)
    all_passwords.append("".join(pwd))

with open("passwords.txt", "w") as opfl:
    opfl.write("\n".join(all_passwords))

# for i in [0, 2]:
#     print(f"[{i}] is the current index")


# ----- 


