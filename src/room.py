# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, location, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = items

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
