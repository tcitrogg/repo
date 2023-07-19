# # def say():
# #     print("Yo! name is Radiance")

# # say()

# # def say(text):
# #     print(f"say: {text}")

# # say(text="Yo! still thinking")

# # def pt(text, prompt):
# #     print(f"{prompt}: {text}")


# # pt(text="Welcome to domain", prompt="Jarvis")

# def pt(text, prompt="Jarvis"):
#     print(f"{prompt}: {text}")


# # pt(text="Welcome to domain", prompt="Alfred")

# def print_prompt():
#     print("Alfred: Welcome Master Bruce")

# # print_prompt()

from random import choices, randint
from string import ascii_letters


# def short_url_id():
#     choice_list = choices(ascii_letters, k=7)
#     url_id = "00000".join(choice_list)
#     print(url_id)
    
# short_url_id()

# def short_url_id(length=7):
#     choice_list = choices(ascii_letters, k=length)
#     url_id = "".join(choice_list)
#     print(url_id)
    
# short_url_id(length=11)

def short_url_id(length=randint(7, 11)):
    """ Generate random short url ID like YouTube, Tiktok etc...
    
    yours Yonko
    """
    choice_list = choices(ascii_letters, k=length)
    url_id = "".join(choice_list)
    return url_id
    
# short_url_id(length=26)
my_ytlink = short_url_id()


print(f"Subscribe to my YouTube channel\n https://youtube.com/shorts/{my_ytlink}")
