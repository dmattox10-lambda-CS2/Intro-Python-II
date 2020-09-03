class Item:
    def __init__(self, itemType, name, description):
        self.itemType = itemType
        self.name = name
        self.description = description

    def __str__(self):
        return f'You are holding a/an {self.name}, it {self.description}'


class Key(Item):
    def __init__(self, itemType, name, description):
        super().__init__(itemType, name, description)


class Food(Item):
    def __init__(self, itemType, name, description, servings):
        super().__init__(itemType, name, description)
        self.servings = servings


class Blaster(Item):
    def __init__(self, itemType, name, description, charges=4):
        super().__init__(itemType, name, description)
        self.charges = charges

    def addBattery(self, Battery):
        self.charges += Battery.charges


class Battery(Item):
    def __init__(self, itemType, name, description, charges=4):
        super().__init__(itemType, name, description)
        self.charges = charges
