
# The item.py file contains a set of classes for different items that can be found or used in the text-based adventure game. Here's an overview of each class:

# Item Class:
# This is the base class for all items in the game.
# It has attributes itemType, name, and description.
# The __str__ method provides a string representation of the item.
# Key Class (Inherits from Item):
# Represents a key item in the game.
# Inherits from the Item class and inherits its attributes and methods.
# Food Class (Inherits from Item):
# Represents a food item in the game.
# Inherits from the Item class and adds an additional attribute servings to represent the number of servings the food item provides.
# Blaster Class (Inherits from Item):
# Represents a blaster item in the game.
# Inherits from the Item class and adds an additional attribute charges to represent the number of charges the blaster has.
# Contains a method addBattery to add charges to the blaster.
# Battery Class (Inherits from Item):
# Represents a battery item in the game, which can be used to recharge the blaster.
# Inherits from the Item class and adds an additional attribute charges to represent the number of charges the battery provides.
# These classes provide a framework for handling different types of items in the game, each with its own attributes and behaviors. They allow for a variety of interactions and functionalities within the game world.
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
