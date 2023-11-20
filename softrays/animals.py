
class Dog:
    def __init__(self, name):
        self.name = name
        self.skin_color = "Brown"
        self.is_tall = True
        # self.signature = (hex(hash(f"{self.name}:{self.skin_color}")))
    
    def bark(self):
        print("Woof!")
    
    def fetch(self, item):
        print(f"{self.name}, fetch {item}")

    def dig(self):
        print(f"{self.name}: 🍗 hiding my bone")

