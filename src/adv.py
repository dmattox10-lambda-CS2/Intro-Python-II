from room import Room
from rooms import roomList
from items import itemList
from player import Player, Alien
from item import Item, Key
from tools import Tools
import random

#
# Main
#
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

aliensList = []
name = input('Enter your name.... ')
player = Player(name, roomList['A1'])
# mob1 = Alien(Tools().randomName(), Tools().randomRoom())
# mob2 = Alien(Tools().randomName(), Tools().randomRoom())
# print(f'{mob1.name}, {mob1.current_room}')
# print(f'{mob2.name}, {mob2.current_room}')
print('[q] to quit, [n,e,s,w] to move, [help] for more')


def fight():
    pass


def moveAliens():
    for i, alien in enumerate(aliensList):
        directionsDict = {
            'n_to': alien.current_room.n_to,
            'e_to': alien.current_room.e_to,
            's_to': alien.current_room.s_to,
            'w_to': alien.current_room.w_to
        }
        directionsList = ['n_to', 'e_to', 's_to', 'w_to']
        choice = random.randint(0, len(directionsList) - 1)
        path = directionsDict[directionsList[choice]]
        if path is not None:
            alien.current_room = path
            if alien.current_room.name == 'E5':
                aliensList.pop(i)
        print(f'{alien.current_room.name}')


while True:
    if len(aliensList) < 2:
        alienName = Tools().randomName()
        aliensList.append(Alien(alienName, Tools().randomRoom()))
    print(f'{player}, you have {player.food} food.')
    print(f'{player.current_room.description}')
    print('\n')
    cmd = input(f'Please enter a command... ').split(' ')
    
    if len(cmd) == 1:
        if cmd[0] == 'q':
            exit(0)
        if cmd[0] == 'n':
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
            else:
                print('There is no path in that direction!')

        if cmd[0] == 'e':
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
            else:
                print('There is no path in that direction!')

        if cmd[0] == 's':
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
            else:
                print('There is no path in that direction!')
        if cmd[0] == 'w':
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
            else:
                print('There is no path in that direction!')
        if cmd[0] == 'help':
            print(
                '[use $ITEM] to use an item\n[drop $ITEM] to drop item\n[take $ITEM] to take item')
        if cmd[0] == 'cheat':
            roomList[Player.Location(player)].ListItems()
        if cmd[0] == 'look':
            if itemList['torch'] in player.Items():
                roomList[Player.Location(player)].ListItems()
            else:
                print('Good luck finding anything in the dark!')
        else:
            pass

    if len(cmd) == 2:
        itemcmd = cmd[1]
        if cmd[0] == 'take':
            if itemList['torch'] in player.Items():
                if itemList[itemcmd] in player.current_room.Items():
                    player.current_room.AddItemToPlayer(
                        itemList[itemcmd], player)
                else:
                    print(f'Didnt find {itemcmd}')
            elif itemcmd == 'torch':
                # print(roomList[Player.Location(player)].Items()) # Prints OBJECT
                if itemList[itemcmd] in player.current_room.Items():
                    # print(roomList[Player.Location(player)].Items()) # Prints nothing
                    player.current_room.AddItemToPlayer(
                        itemList[itemcmd], player)
            else:
                print('Good Luck finding that in the dark!')
        elif cmd[0] == 'drop':
            if itemList[itemcmd] in player.items:
                player.Drop(itemList[itemcmd], player.current_room)
        elif cmd[0] == 'use':
            if itemList[itemcmd] in player.items:
                if itemList[itemcmd].name == 'torch':
                    player.current_room.ListItems()
                elif itemList[itemcmd].name == 'test':
                    print('The system is working!')
                elif itemList[itemcmd].name == 'blaster':
                    index = None
                    for i in range(len(player.Items())):
                        if player.Items()[i].name == 'blaster':
                            index = i
                    if player.Items()[i].charges > 0:
                        player.Items()[i].charges -= 1
                        shots = player.Items()[i].charges
                        print(
                            f'You fired your blaster! It has {shots} shots left!')
                    else:
                        print(f'Your blaster doesn\'t function!')
                else:
                    pass
        else:
            pass

    if player.current_room.name == 'E5':
        print('You win!')
        exit(0)

    moveAliens()
