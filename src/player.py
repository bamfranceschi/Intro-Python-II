# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f"{self.name}, your current room is: {self.current_room}"

    def take_item(self, item):
        # self.item = item
        self.inventory.append(item)
        # return f"took {self.item}"

    def drop_item(self, item):
        self.inventory.remove(item)


# print(first_player)

##move on player
##get/drop on player
