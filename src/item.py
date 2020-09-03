class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'You are holding a/an {self.name}, it {self.description}'


class Key(Item):
    def __init__(self, name, description, door):
        super().__init__(name, description)
        self.door = door


class Food(Item):
    def __init__(self, name, description, servings):
        super().__init__(name, description)
        self.servings = servings


class Blaster(Item):
    def __init__(self, name, description, charges=4):
        super().__init__(name, description)
        self.charges = charges

    def addBattery(self, Battery):
        self.charges += Battery.charges


class Battery(Item):
    def __init__(self, name, description, charges=4):
        super().__init__(name, description)
        self.charges = charges
