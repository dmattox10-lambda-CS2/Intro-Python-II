
# The items.py file contains a dictionary called itemList which maps item names to instances of different item classes. Each item has a unique name, item type, and description. Here's a breakdown of the items defined in the itemList dictionary:

# torch: An instance of the Item class representing a torch that lights the way.
# test: An instance of the Item class used for testing purposes.
# blaster: An instance of the Blaster class representing a DL-44 blaster. It has a limited number of charges.
# battery: An instance of the Battery class representing a battery for the blaster. It can recharge the blaster.
# red, blue, green: Instances of the Key class representing different colored key cards.
# apple, banana, twinkies, jerky, MRE, bar, chips, cake, sandwich, chocolate: Instances of the Food class representing different types of food items with varying numbers of servings.
# Additionally, the code snippet adds some of these items to specific rooms within the game world using the AddItemToRoom method of the Room class. For example:

# Torch, test, and blaster are added to room 'A1'.
# Batteries are added to rooms 'B2' and 'C3'.
# This setup ensures that these items are available for players to interact with when exploring the corresponding rooms in the game.

from rooms import roomList
from item import Item, Key, Food, Blaster, Battery

itemList = {
    'torch': Item('torch', 'torch', 'Lights the way!'),
    'test': Item('test', 'test', 'Wait, that\'s not supposed to be here!'),
    'blaster': Blaster('blaster', 'blaster', 'DL-44! Han shot first, use it wisely!'),
    'battery': Battery('battery', 'battery', 'Battery for the blaster'),
    'red': Key('key', 'red', 'Red Key Card'),
    'blue': Key('key', 'blue', 'Blue Key Card'),
    'green': Key('key', 'green', 'Green Key Card'),
    'apple': Food('food', 'apple', 'Apple', 1),
    'banana': Food('food', 'banana', 'Banana', 1),
    'twinkies': Food('food', 'twinkies', 'Twinkies - They never go bad', 2),
    'jerky': Food('food', 'jerky', 'Beef Jerky', 5),
    'MRE': Food('food', 'MRE', 'MRE', 2),
    'bar': Food('food', 'bar', 'Protein Bar', 2),
    'chips': Food('food', 'chips', 'Chips, mostly air', 1),
    'cake': Food('food', 'cake', 'The cake is NOT a lie!', 8),
    'sandwich': Food('food', 'sandwich', 'Sandwich, old, but it\'s better than starving', 2),
    'chocolate': Food('food', 'chocolate', 'Chocolate?', 1)
}

roomList['A1'].AddItemToRoom(itemList['torch'])
roomList['A1'].AddItemToRoom(itemList['test'])
roomList['A1'].AddItemToRoom(itemList['blaster'])
roomList['B2'].AddItemToRoom(itemList['battery'])
roomList['C3'].AddItemToRoom(itemList['battery'])