import random
from string import ascii_letters
# import pyttsx4

# engine = pyttsx4.init()
# engine.say("Welcome Master Tony")
# engine.runAndWait()

"https://www.youtube.com/watch?v=FvIdpJx8WWc"

def short_url_id(length=random.randint(7, 11)):
    random_list = random.choices(ascii_letters, k=length)
    url_id = "".join(random_list)
    return url_id

# short_url_id(15)
my_link = short_url_id()


# print(f"""
#       Subscribe to my Softrays Channel
#       https://www.softraysit.com/watch?v={my_link}
#        """)

# Assert
print(len(my_link), my_link)
assert len(my_link) == 9, "(x) my_link is not 9 chars long"