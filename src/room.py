# Implement a class to hold room information. This should have name and
# description attributes.

# The Room class has been implemented to hold information about each room in the game. Here's an overview of its structure:

# Attributes:
# name: Name of the room.
# description: Description of the room.
# n_to, e_to, s_to, w_to: Pointers to neighboring rooms in the north, east, south, and west directions respectively.
# items: List of items present in the room.
# Methods:
# Items(): Returns the list of items present in the room.
# ListItems(): Prints out the names of the items present in the room.
# AddItemToRoom(item): Adds an item to the list of items present in the room.
# AddItemToPlayer(item, player): Adds an item to the player's inventory if it is present in the room and removes it from the room's list of items.
# interact(item, player): Placeholder method for handling interactions with items in the room.
# __str__(): Returns a string representation of the room, including its name and description.
# This class provides a foundation for representing and interacting with rooms within the game environment. Additional functionality for interactions and navigation between rooms can be built upon this class as needed.
class Room:
    def __init__(self, name, location, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []

    def Items(self):
        return self.items

    def ListItems(self):
        for item in self.items:
            print(f'This room contains a/an {item.name}')

    def AddItemToRoom(self, item):
        self.items.append(item)

    def AddItemToPlayer(self, item, player):
        if item in self.items:
            self.items.remove(item)
            player.AddItem(item)

    def interact(self, item, player):
        pass

    def __str__(self):
        return f'current location: {self.name}, {self.description}'
