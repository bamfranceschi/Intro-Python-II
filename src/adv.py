from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

first_player = Player("Gandalf", room["outside"])
print(f"Welcome, {first_player.name}, to the adventure of the ages. You are currently {first_player.current_room}.")


while True:
    direction = input("Do you want to go north(n), south(s), east(e) or west(w)?")

    if direction == "n":
        first_player.current_room = first_player.current_room.n_to
        print("\ncurrent room: %s \n\ndescription: %s\n" %(first_player.current_room.name, first_player.current_room.desc))
    elif direction == "s":
        first_player.current_room = first_player.current_room.s_to
        print("\ncurrent room: %s \n\ndescription: %s\n" %(first_player.current_room.name, first_player.current_room.desc))
    elif direction == "w":
        first_player.current_room = first_player.current_room.w_to
        print("\ncurrent room: %s \n\ndescription: %s\n" %(first_player.current_room.name, first_player.current_room.desc))
    elif direction == "e":
        first_player.current_room = first_player.current_room.e_to
        print("\ncurrent room: %s \n\ndescription: %s\n" %(first_player.current_room.name, first_player.current_room.desc))
    elif direction == "q":
        print("Goodbye!")
        quit()
    else:
        print("Please provide a direction or q to quit") 


#for key, value in room.items():
#     if first_player.in_room == key:
#         print("\ncurrent room: %s \n\ndescription: %s\n" %(value.name, value.desc))

# 
