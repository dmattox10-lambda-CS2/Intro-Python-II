# Write a class to hold player information, e.g. what room they are in
# currently.
# Player Class:
# Attributes:
# name: Name of the player.
# current_room: The room where the player is currently located.
# items: List of items the player is carrying.
# food: Amount of food the player has.
# health: Player's health points.
# Methods:
# Eat(): Decreases the player's food by 1. If food reaches 0, the player starves to death.
# AddItem(item): Adds an item to the player's inventory and adjusts food accordingly for food items. If the item is poisoned chocolate, the player's food is halved and they get sick.
# Drop(item, room): Drops an item from the player's inventory into the specified room.
# Items(): Returns the list of items the player is carrying.
# Location(): Returns the name of the room where the player is located.
# Surroundings(): Returns the description of the current room.
# TakeWound(): Placeholder method for handling player wounds.
# Heal(): Placeholder method for healing the player.
# __str__(): Returns the player's name.
# Alien Class (Inherits from Player):
# Represents an alien character in the game.
# Inherits from the Player class and inherits its attributes and methods.
# Additional methods or attributes specific to aliens can be added in the future.
# Both classes provide a framework for handling player and alien characters in the game, including their attributes, methods for interacting with items and the environment, and placeholder methods for future expansion.
import math


class Player:
    def __init__(self, name, current_room, items=[], food=5, health=10):
        self.name = name
        self.current_room = current_room
        self.items = items
        self.food = food
        self.health = health

    def Eat(self):
        self.food -= 1
        if self.food == 0:
            print(f'You starved to death.')
            exit(0)

    def AddItem(self, item):
        self.items.append(item)
        print(f'Got item {item.name}!')
        print(f'{item.description}')
        if item.itemType == 'food':
            self.food += item.servings
        if item.description == 'Chocolate?':
            self.food = math.floor(self.food / 2)
            print(f'The chocolate was poisoned, you wretch all over the place!')
        if item.name == 'battery':
            if 'blaster' in self.items:
                index = None
                for i, entry in enumerate(self.items):
                    if self.items[i].name == 'blaster':
                        index = i
                    blaster = self.items[i]
                    blaster.addBattery(item)

    def Drop(self, item, room):
        if item in self.items:
            self.items.remove(item)
            room.AddItemToRoom(item)
            print(f'Dropped item {item.name}')
        else:
            print(f'Not holding item {item.name}')

    def Items(self):
        return self.items  # Clean this up

    def Location(self):
        return self.current_room.name  # Clean this up

    def Surroundings(self):
        return self.current_room.description  # Does this need cleaned up?

    def TakeWound(self):
        pass

    def Heal(self):
        pass

    def __str__(self):
        return self.name  # Expand on this


class Alien(Player):
    def __init__(self, name, current_room, items=[], health=3):
        super().__init__(name, current_room, items, health)

    def Shoot(self):
        pass
