import random

class Human:
    def __init__(self, name, age, skin_color, gender):
        self.name = name
        self.age = age
        self.skin_color = skin_color
        self.gender = gender
        self.favorite_food = ["Garri", "Spag", "Rice", "Beans and Bread"]
        self.cry()

    def cry(self):
        print("Uhwwwww!")

    def cook(self):
        print(random.choice(self.favorite_food))

mary = Human(name="Mary", age=20, skin_color="Brown", gender="Female")
mary.favorite_food = ["Burger", "Shawarma", "Pizza", "Ice cream"]

mary.cook()
# print(mary.)
