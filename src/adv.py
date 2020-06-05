from room import Room
from player import Player
from item import Item

# Items

items = {
    "sword": Item(
        "Glamdring",
        "a hand-and-a-half sword, forged for Turgon, the Elven King of Gondolin during the First Age, and much later owned by the wizard Gandalf.",
    ),
    "ring": Item(
        "Nenya",
        "also known as the White Ring, the Ring of Adamant, and the Ring of Water, was one of the Rings of Power, specifically, one of the Three Rings of the Elves of Middle-earth.",
    ),
    "bow": Item(
        "Greenleaf",
        "a masterful bow and slayer of orcs, wraiths, and other foul beasts.",
    ),
    "axe": Item(
        "Lockbearer", "a dwarven-crafted broad-bladed axe that is exceptionally heavy."
    ),
    "brooch": Item(
        "Evenstar",
        "Arwen's famous necklace that she gave Aragorn as a symbol of her love and her choice of mortality.",
    ),
    "stone": Item(
        "Palantir",
        "a spherical stone object used for the purpose of communication in Middle-earth. ",
    ),
    "bread": Item(
        "Lembas",
        "also called Elven bread or Waybread in the Common Speech, was a special travel-food made by the Elves",
    ),
    "chainmail": Item(
        "Mithril",
        "a chainmail shirt made from a precious, silvery metal (mithril), very lightweight but immensely strong, that was mined by the Dwarves in Khazad-dûm",
    ),
    "torch": Item("Torch", "a stick on fire, that helps you see in the dark."),
}

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons",),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
        items["axe"],
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        [items["ring"], items["brooch"]],
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        [items["chainmail"], items["sword"]],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        items["bread"],
    ),
}

## add items to rooms here. is that the problem?

room["outside"].add_item(items["bow"])
room["outside"].add_item(items["stone"])
room["foyer"].add_item(items["axe"])
room["overlook"].add_item(items["ring"])
room["overlook"].add_item(items["brooch"])
room["narrow"].add_item(items["chainmail"])
room["narrow"].add_item(items["sword"])
room["treasure"].add_item(items["bread"])

# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]


first_player = Player("Gandalf", room["outside"])
first_player.take_item(items["torch"])


def location():
    print(
        f"You are currently at {first_player.current_room.name}. \n{first_player.current_room.desc}. \nItems available here: \n\n"
    )


def found_item():
    for e in first_player.current_room.stash:
        print("- %s" % (e) + " \n")


def start_game():

    print(f"Welcome, {first_player.name}, to the adventure of the ages.")
    location()
    found_item()


def display_items():

    for i in first_player.inventory:
        print(f"- {i.name}")


user_is_playing = True

start_game()

while user_is_playing:

    action = input(
        "Do you want to take or drop an item? To take an item, enter [take] [item-name]. To drop an item, enter [drop] [item-name]. If not, enter [no thank you]. To see your inventory, enter [i] or [inventory] "
    )

    for i in first_player.current_room.stash:
        if action == "take %s" % (i.name):
            first_player.take_item(i)
            i.on_take()
            first_player.current_room.remove_item(i)

    for n in first_player.inventory:
        if action == "drop %s" % (n.name):
            first_player.drop_item(n)
            n.on_drop()
            first_player.current_room.add_item(n)

    if action == "i" or "inventory":
        display_items()
    elif action == "no thank you":
        pass

    direction = input("Where do you want to go? [n/s/e/w] \n").lower()

    if direction == "n":
        if first_player.current_room.n_to is not None:
            first_player.current_room = first_player.current_room.n_to
            location()
            found_item()
        else:
            print("Warning! You can't go that way")
    elif direction == "s":
        if first_player.current_room.s_to is not None:
            first_player.current_room = first_player.current_room.s_to
            location()
            found_item()
        else:
            print("Warning! You can't go that way")
    elif direction == "w":
        if first_player.current_room.w_to is not None:
            first_player.current_room = first_player.current_room.w_to
            location()
            found_item()
        else:
            print("Warning! You can't go that way")
    elif direction == "e":
        if first_player.current_room.e_to is not None:
            first_player.current_room = first_player.current_room.e_to
            location()
            found_item()
        else:
            print("Warning! You can't go that way")
    elif direction == "q":
        print("Goodbye!")
        user_is_playing = False
        quit()
    else:
        print("Please provide a direction or q to quit")


# for key, value in room.items():
#     if first_player.in_room == key:
#         print("\ncurrent room: %s \n\ndescription: %s\n" %(value.name, value.desc))

#


######
# need an item dict - DONE
# need a class for item -DONE
# need to add item lists on both room and player -DONE
# need to be able to remove items from either list
