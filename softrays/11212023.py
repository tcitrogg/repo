class Parent:
    def __init__(self):
        self.skin_color = "Brown"
        self.eye_color = "Blue"
        self.hair_color = "Red"
        self.nose_type = "Flat"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.eye_color = "Green"
        self.hair_color = "Red and White"


# son = Child()
# print(son.nose_type)


# Polymorphism

class Human:
    def __init__(self):
        self.skin_color = "Brown"
        self.eye_color = "Blue"
        self.hair_color = "Red"
        self.nose_type = "Flat"
        self.chromosome = "XY"

class Female:
    def __init__(self):
        self.skin_color = "Black"
        self.eye_color = "Green"
        self.hair_color = "Blonde"
        self.nose_type = "Round"
        self.chromosome = "XX"

person = Human()
woman = Female()

def get_hair_color(object):
    print(object.hair_color)

# get_hair_color(person)
# get_hair_color(woman)

# for obj in (person, woman):
#     print(obj.hair_color)

# Decorators
def say(func):
    def talk_to_me():
        print("Kamehameha!")
        func()
    return talk_to_me

@say
def run():
    print("The rabbit")

# run()


class Staff:
    def __init__(self, name, age, role="Staff", department="Dept"):
        self.name = name
        self.age = age
        self.role = role
        self.department = department

    def about(self):
        print(f"""Name: {self.name}
Age:  {self.age}
Role: {self.role}
Dept: {self.department}
""")

class TeachingStaff(Staff):
    def __init__(self, name, age, role="Staff", department="Dept"):
        super().__init__(name, age, role, department)

class NonTeachingStaff(Staff):
    def __init__(self, name, age, role="Staff", department="Dept"):
        super().__init__(name, age, role, department)

tim = TeachingStaff("Tim Ton", age=25, role="TeachingStaff", department="Science")
susan = NonTeachingStaff("Susan Bills", age=26, role="NonTeachingStaff", department="Library")

# tim.about()
# susan.about()





# Tasks: Bank Account
from datetime import datetime

class Ichimonji:
    title = "Ichimonji"
    currency = "{0}"

    def __init__(self, name):
        self.name = name
        sign_number = hash(f"{name}:{datetime.now()}")
        if sign_number < 0:
            self.account_number = hex(-sign_number)
        else:
            self.account_number = hex(sign_number)
        self.balance = 0
        self.datetime = datetime.now()
    
    def check_balance(self):
        print(self.balance)
    
    def transfer(self, amount, account_number):
        if amount > self.balance:
            print("(x) Error | Insufficent balance")
        else:
            self.balance -= amount
            print(f"(+) Successful | tranferred *{self.currency}{amount}* to {account_number}")
    
    def print_card(self):
        # print("|  {:8}  |".format(f"Account Number: {self.account_number}"))
        card = f"""/-----------------------------------------\\
|  {"{0}"} {self.title}.net                      |
|                                         |
|  Account Number: {self.account_number}     |
|               100101010101001010101010  |
\\_________________________________________/
"""
        print(card)

    def profile(self):
        print(f"""{self.currency} {self.title}
""")

wallet_one = Ichimonji(name="Radiance")
wallet_one.balance = 9_000_000_000
# print(wallet_one.account_number)
wallet_one.print_card()

# print(hex(hash(f"{name}:{age}")))