from rooms import roomList
from item import Item, Key, Food, Blaster, Battery

itemList = {
    'torch': Item('torch', 'torch', 'Lights the way!'),
    'test': Item('test', 'test', 'Tests the system!'),
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
# roomList['A1'].AddItemToRoom(itemList['test'])
# roomList['A1'].AddItemToRoom(itemList['blaster'])
# roomList['B2'].AddItemToRoom(itemList['battery'])
# roomList['C3'].AddItemToRoom(itemList['battery'])