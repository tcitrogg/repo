# Tinu the cat as an object
class Cat:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color

    def meow(self):
        print(f"{self.name}: Meow!")

# tinu = Cat("Tinu", "White")
# tinu.meow()

# pwd gen in oop
import random
import string

class Passgen:
    def __init__(self, amount=1, length=8, no_uppercase=0, no_lowercase=0, no_punctuation=0, no_digits=0):
        self.amount = amount
        self.length = length
        self.no_uppercase = no_uppercase
        self.no_lowercase = no_lowercase
        self.no_punctuation = no_punctuation
        self.no_digits = no_digits

    def gen(self):
        pwd = []
        fillup = []
        sum_of_chars = self.no_digits + self.no_lowercase + self.no_uppercase + self.no_punctuation
        if self.no_digits == 0 and self.no_lowercase == 0 and self.no_uppercase == 0 and self.no_punctuation == 0:
            pwd = random.choices(
                string.ascii_letters+f"{string.digits}"+string.punctuation,
                k=self.length
            )
        else:
            if sum_of_chars < self.length:
                if self.no_digits == 0:
                    fillup += random.choices(string.digits,  k=random.randint(1,9))
                else:
                    pwd += random.choices(string.digits,  k=self.no_digits)
                if self.no_uppercase == 0:
                    fillup += random.choices(string.ascii_uppercase,  k=random.randint(1,9))
                else:
                    pwd += random.choices(string.ascii_uppercase,  k=self.no_uppercase)
                if self.no_lowercase == 0:
                    fillup += random.choices(string.ascii_lowercase,  k=random.randint(1,9))
                else:
                    pwd += random.choices(string.ascii_lowercase,  k=self.no_lowercase)
                if self.no_punctuation == 0:
                    fillup += random.choices(string.punctuation,  k=random.randint(1,9))
                else:
                    pwd += random.choices(string.punctuation,  k=self.no_punctuation)

                pwd += random.choices(fillup,  k=self.length-sum_of_chars)
        return "".join(pwd)

p = Passgen(no_punctuation=2)
my_secret_password = p.gen()

print(f"my_secret_password: {my_secret_password}")

# inheritance
