from rooms import roomList
from items import itemList
from room import Room
from item import Item, Key, Food, Blaster, Battery
import random

# The tools.py file contains a Tools class with two methods designed to provide random functionality for the game:

# randomName(self):
# Generates a random name for characters or entities in the game.
# Parameters: None.
# Returns: A randomly generated name consisting of uppercase letters and numbers with a length between 3 and 12 characters.
# randomRoom(self):
# Selects a random room from the roomList dictionary.
# Parameters: None.
# Returns: A randomly selected Room object from the roomList.
# These methods can be utilized within the game to generate random names for characters or to randomly select rooms for various purposes. For example, the randomRoom() method could be used to place items or NPCs in different locations within the game world.

# The class constructor (__init__) is empty as it doesn't require any initialization logic. The class simply serves as a container for these two utility methods.


class Tools:
    def __init__(self):

        pass

    def randomName(self):
        length = random.randint(3, 12)
        characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
        name = ''
        for i in range(length):
            selection = random.randint(0, len(characters) - 1)
            name += characters[selection]
        return name

    def randomRoom(self):
        roomAddresses = []
        for k in roomList.keys():
            roomAddresses.append(k)
        roomSelection = random.randint(5, len(roomAddresses) - 1)
        return roomList[roomAddresses[roomSelection]]
