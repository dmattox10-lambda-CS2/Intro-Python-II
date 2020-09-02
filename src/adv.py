from room import Room
from rooms import roomList, itemList
from player import Player
from item import Item, Key

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

name = input('Enter your name.... ')
player = Player(name, roomList['A1'])
print('[q] to quit, [n,e,s,w] to move, [help] for more')
while True:
    print('\n')
    cmd = input(f'{player}, enter a command... ').split(' ')

    if len(cmd) == 1:
        if cmd[0] == 'q':
            exit(0)
        if cmd[0] == 'n':
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
                print(f'{player.current_room.description}')
            else:
                print('There is no path in that direction!')

        if cmd[0] == 'e':
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
                print(f'{player.current_room.description}')
            else:
                print('There is no path in that direction!')

        if cmd[0] == 's':
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
                print(f'{player.current_room.description}')
            else:
                print('There is no path in that direction!')
        if cmd[0] == 'w':
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
                print(f'{player.current_room.description}')
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
                if itemList[itemcmd].name == 'test':
                    print('The system is working!')
                else:
                    pass
        else:
            pass

    if player.current_room.name == 'E5':
        print('You win!')
        exit(0)
