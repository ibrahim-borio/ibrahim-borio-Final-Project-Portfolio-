class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def showInfo(self):
        print(f"Player: {self.name}, Level: {self.level}")

class Warrior(Player):
    def __init__(self, name, level, power):
        super().__init__(name, level)
        self.power = power

    def showInfo(self):
        super().showInfo()
        
        print("Role: Warrior")
        print(f"Power: {self.power}")
        
class magic(Player):
    def __init__(self, name, level, magic):
        super().__init__(name, level)
        self.level = level
        self.magic = magic

    def showInfo(self):
        super().showInfo()
        print("Role: Magic")
        print(f"Magic level is {self.level}")
        print(f"Magic power is {self.magic}")



omar = magic("Omar", 84, "Fire")
omar.showInfo()