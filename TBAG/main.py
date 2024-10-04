from room import Room
from character import Enemy, Friend
from item import Key, Sword

hallway = Room("Hallway")
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")

hallway.set_description("A narrow hallway with broken lights and moldy ceilings.")
kitchen.set_description("A smelly kitchen with greasy walls, stale air, and a foul stench.")
ballroom.set_description("This ballroom smells like dead people.")

hallway.link_room(kitchen, "north")
hallway.link_room(ballroom, "east")
kitchen.link_room(hallway, "south")

ballroom.locked = True

dave = Enemy("Dave", "An Evil, Decaying zombie. Craves brains. Makes witty remarks.")
dave.set_conversation("You… have brains… and I'm on a strict brain-only diet!")
dave.set_weakness("sword")
ballroom.set_character(dave)

alice = Friend("Alice", "A ghost who silently observes from the shadows, offering protection but also has an unsettling presence.")
alice.set_conversation("Hello! I'm Alice. If you answer my questions correctly, I'll give you some useful items which will help you escape.")
kitchen.set_character(alice)

rusty_key = Key()
rusty_key.set_name("rusty key")
sword = Sword()
sword.set_name("sword")

current_room = hallway
inventory = []
tries = 3

def handle_room_transition(current_room, direction, inventory):
    next_room = current_room.move(direction)
    if next_room.locked:
        if "rusty key" in inventory:
            print("You use the rusty key to unlock the door.")
            next_room.locked = False
        else:
            print("The door is locked. You need a rusty key.")
            return current_room
    return next_room

while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant:
        inhabitant.describe()
        if isinstance(inhabitant, Enemy):
            print("You can: [Fight]")
        elif isinstance(inhabitant, Friend):
            print("You can: [Talk, Sword, Key, South]")
    else:
        print("You can: [Move]")

    command = input("> ").lower()
    if command in ["north", "south", "east", "west"]:
        current_room = handle_room_transition(current_room, command, inventory)
    elif command == "talk":
        if inhabitant and isinstance(inhabitant, Friend):
            inhabitant.talk()
            hug = input("Alice: Would you mind giving a lonely spirit a hug? [yes/no] ").lower()
            if hug == "yes":
                print("Alice gives you a warm hug and whispers: 'Be cautious of the zombie and use the sword to kill him.'")
            else:
                print("Alice looks sad. Suddenly, you feel a chill and everything goes dark. You are dead. Game Over!")
                exit()
        else:
            print("Please try again.")
    elif command == "sword":
        if inhabitant and isinstance(inhabitant, Friend):
            print("You pick up a mystical sword.")
            inventory.append("sword")
        else:
            print("There is no sword here to pick up.")
    elif command == "key":
        if inhabitant and isinstance(inhabitant, Friend):
            print("You pick up a rusty key.")
            inventory.append("rusty key")
        else:
            print("There is no key here to pick up.")
    elif command == "fight":
        if inhabitant and isinstance(inhabitant, Enemy):
            while tries > 0:
                print("Which attack will you use? [Punch, Kick, Sword]")
                fight_with = input("> ").lower()
                if fight_with == "sword" and "sword" in inventory:
                    print("You swing the mystical sword and you chop Dave's head clean off!")
                    ballroom.set_character(None)
                    break
                else:
                    tries -= 1
                    if tries > 0:
                        print(f"Wrong attack! You have {tries} tries left.")
                    else:
                        print("Dave rips your head off and feasts on your brains. Game Over!")
                        exit()
   
            while True:
                print("You can: [West, Exit]")
                command = input("> ").lower()
                if command == "west":
                    current_room = hallway
                    break
                elif command == "exit":
                    print("You find a secret exit and escape to safety. Congratulations, you have completed the game. The End")
                    exit()
                else:
                    print("Invalid command. You can only go back to the hallway or exit.")
        else:
            print("There is no one here to fight.")
    elif command == "exit":
        print("You can't exit from here.")
    else:
        print("Invalid command.")
