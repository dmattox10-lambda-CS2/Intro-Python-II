# Write a class to hold player information, e.g. what room they are in
# currently.
import math


class Player:
    def __init__(self, name, current_room, items=[], food=5):
        self.name = name
        self.current_room = current_room
        self.items = items
        self.food = food

    def Eat(self):
        self.food -= 1
        if self.food == 0:
            print(f'You starved to death.')
            exit(0)

    def AddItem(self, item):
        self.items.append(item)
        print(f'Got item {item.name}!')
        print(f'{item.description}')
        if item.name == 'Food':
            self.food += item.servings
        if item.description == 'Chocolate?':
            self.food = math.floor(self.food / 2)
            print(f'The chocolate was poisoned, you wretch all over the place!')

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

    def __str__(self):
        return self.name  # Expand on this


class Alien(Player):
    def __init__(self, name, current_room, alive=True):
        super().__init__(name, current_room, alive)
        self.alive = alive
