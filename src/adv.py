from room import Room
from player import Player
from item import Item
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [
                         Item("Dagger", "A basic dagger"),
                         Item("Sheild", "Super strong Shield")
                     ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [
                         Item("Sword", "Strong silver sword!")
                     ]),

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(input("What's your name? "), room['outside'])

fullDirection = {
    "n": "North",
    "e": "East",
    "s": "South",
    "w": "West",
}


def nextRoom(dir, currentRoom):
    direction = dir + "_to"
    return getattr(currentRoom, direction)


def movePlayer(ply, dir):
    room = nextRoom(dir, ply.currentRoom)
    if room:
        ply.currentRoom = room
        print(
            f"Moved {fullDirection[dir]} and are in a new Room!")
        return True
    else:
        return False


finished = False
helpOptions = "Options: \n  n, e, s, w: the possible directions\n  get/take ITEMNAME: picks up an item\n  drop ITEMNAME: drops the item\n  i: lists your items in your inventory\n  q: quits the game\n  h: gives you Help options"
print(f"Lets Begin {player.name}\n{helpOptions}")


while not finished:
    print(player.currentRoom)
    commands = input(
        "Pick a Direction or pick up and drop an item: ").lower().split(" ")
    if commands[0] in ["n", "e", "s", "w"]:
        if movePlayer(player, commands[0]):
            continue
        else:
            print("No Room in that Direction")
            continue
    elif commands[0] in ["take", "get"]:
        whichItem = player.pickupItem(commands[1])
        # print(whichItem)
        if not whichItem:
            print(
                f"Item {commands[1]} is not in this room")
            continue
    elif commands[0] == "drop":
        item = player.dropItem(commands[1])
        if not item:
            print(f"You don't have a {commands[1]}")
            continue
    elif commands[0] in ["i", "inventory"]:
        print(player.inventoryString())
        continue
    elif commands[0] == "q":
        finished = True
        continue
    elif commands[0] == "h":
        print(helpOptions)
        continue
    else:
        print("This command doesn't exist")
        continue
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
