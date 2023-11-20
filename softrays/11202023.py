
class Stack:
    rack = []
    def __init__(self) -> None:
        pass

    def push(self, item) -> None:
        self.rack.append(item)

    def pop(self) -> any:
        popped_item = self.rack[-1]
        self.rack = self.rack[:-1]
        return popped_item

# vm = Stack()
# vm.push("read")
# vm.push("write")
# vm.push("own")


# print(vm.pop())
# print(vm.rack)


from animals import Dog

class Pitbull(Dog):
    def __init__(self, name):
        super().__init__(name)
        self.skin_color = "Brown and White"
        self.is_tall = False


pet = Pitbull("Flash")
pet.skin_color = "Black"
print(pet.skin_color)