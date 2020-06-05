# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc, stash=None):
        self.name = name
        self.desc = desc
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.stash = []

    def __str__(self):
        return f"{self.name}, {self.desc}."

    def add_item(self, item):
        self.stash.append(item)
        return f"new item added: {self.stash}"

    def remove_item(self, item):
        # self.item = item
        self.stash.remove(item)
        # return f"item removed: {self.item}"
