from room import Room
from item import Item, Key, Food, Blaster, Battery

roomList = {
    'A1': Room('A1', "Room A1", "On the floor in the center of the room is an engraving: A1. There is passage to the East "),
    'B1': Room('B1', "Room B1", "On the floor in the center of the room is an engraving: B1. There is a passage to the West, North, and East "),
    'C1': Room('C1', "Room C1", "On the floor in the center of the room is an engraving: C1. There is a passage to the West, and East "),
    'D1': Room('D1', "Room D1", "On the floor in the center of the room is an engraving: D1. There is a passage to the West, and East "),
    'E1': Room('E1', "Room E1", "On the floor in the center of the room is an engraving: E1. There is a passage to the West "),
    'A2': Room('A2', "Room A2", "On the floor in the center of the room is an engraving: A2. There is a passage to the East "),
    'B2': Room('B2', "Room B2", "On the floor in the center of the room is an engraving: B2. There is a passage in all four directions "),
    'C2': Room('C2', "Room C2", "On the floor in the center of the room is an engraving: C2. There is a passage to the West, and East "),
    'D2': Room('D2', "Room D2", "On the floor in the center of the room is an engraving: D2. There is a passage to the West "),
    'E2': Room('E2', "Room E2", "On the floor in the center of the room is an engraving: E2. There is a passage to the North "),
    'A3': Room('A3', "Room A3", "On the floor in the center of the room is an engraving: A3. There is a passage to the East"),
    'B3': Room('B3', "Room B3", "On the floor in the center of the room is an engraving: B3. There is a passage to the West, East, and South "),
    'C3': Room('C3', "Room C3", "On the floor in the center of the room is an engraving: C3. There is a passage to the West, North, and East "),
    'D3': Room('D3', "Room D3", "On the floor in the center of the room is an engraving: D3. There is a passage to the West, and East "),
    'E3': Room('E3', "Room E3", "On the floor in the center of the room is an engraving: E3. There is a passage to the West, and South "),
    'A4': Room('A4', "Room A4", "On the floor in the center of the room is an engraving: A4. There is a passage to the East "),
    'B4': Room('B4', "Room B4", "On the floor in the center of the room is an engraving: B4. There is a passage to the West, and East "),
    'C4': Room('C4', "Room C4", "On the floor in the center of the room is an engraving: C4. There is a passage to the West, East, and South"),
    'D4': Room('D4', "Room D4", "On the floor in the center of the room is an engraving: D4. There is a passage to the West, and East"),
    'E4': Room('E4', "Room E4", "On the floor in the center of the room is an engraving: E4. There is a passage to the West, and North"),
    'E5': Room('E5', "Room E5", "You've exited the maze!")
}

roomList['A1'].e_to = roomList['B1']
roomList['B1'].w_to = roomList['A1']
roomList['B1'].n_to = roomList['B2']
roomList['B1'].e_to = roomList['C1']
roomList['C1'].w_to = roomList['B1']
roomList['C1'].e_to = roomList['D1']
roomList['D1'].w_to = roomList['C1']
roomList['D1'].e_to = roomList['E1']
roomList['E1'].w_to = roomList['D1']
roomList['A2'].e_to = roomList['B2']
roomList['B2'].w_to = roomList['A2']
roomList['B2'].n_to = roomList['B3']
roomList['B2'].e_to = roomList['C2']
roomList['B2'].s_to = roomList['B1']
roomList['C2'].w_to = roomList['B2']
roomList['C2'].e_to = roomList['D2']
roomList['D2'].w_to = roomList['C2']
roomList['E2'].n_to = roomList['E3']
roomList['A3'].e_to = roomList['B3']
roomList['B3'].w_to = roomList['A3']
roomList['B3'].e_to = roomList['C3']
roomList['B3'].s_to = roomList['B2']
roomList['C3'].w_to = roomList['B3']
roomList['C3'].n_to = roomList['C4']
roomList['C3'].e_to = roomList['D3']
roomList['D3'].w_to = roomList['C3']
roomList['D3'].e_to = roomList['E3']
roomList['E3'].w_to = roomList['D3']
roomList['E3'].s_to = roomList['E2']
roomList['A4'].e_to = roomList['B4']
roomList['B4'].w_to = roomList['A4']
roomList['B4'].e_to = roomList['C4']
roomList['C4'].w_to = roomList['B4']
roomList['C4'].e_to = roomList['D4']
roomList['C4'].s_to = roomList['C3']
roomList['D4'].w_to = roomList['C4']
roomList['D4'].e_to = roomList['E4']
roomList['E4'].n_to = roomList['E5']

itemList = {
    'torch': Item('torch', 'Lights the way!'),
    'test': Item('test', 'Tests the system!'),
    'blaster': Blaster('DL-44', 'Han shot first, use it wisely!'),
    'battery': Battery('DL-44P', 'Battery for the blaster'),
    'apple': Food('Food', 'Apple', 1),
    'banana': Food('Food', 'Banana', 1),
    'twinkies': Food('Food', 'Twinkies - They never go bad', 2),
    'jerky': Food('Food', 'Beef Jerky', 5),
    'MRE': Food('Food', 'MRE', 2),
    'bar': Food('Food', 'Protein Bar', 2),
    'chips': Food('Food', 'Chips, mostly air', 1),
    'cake': Food('Food', 'The cake is NOT a lie!', 8),
    'sandwich': Food('Food', 'Sandwich, old, but it\'s better than starving', 2),
    'chocolate': Food('Food', 'Chocolate?', 1)
}

roomList['A1'].AddItemToRoom(itemList['torch'])
roomList['A1'].AddItemToRoom(itemList['test'])
roomList['A1'].AddItemToRoom(itemList['blaster'])
roomList['B2'].AddItemToRoom(itemList['battery'])
roomList['C3'].AddItemToRoom(itemList['battery'])
