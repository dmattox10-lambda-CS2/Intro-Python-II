from rooms import roomList
from items import itemList
from room import Room
from item import Item, Key, Food, Blaster, Battery
import random


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
