from room import Room
from character import Enemy
dead = False

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room, buzzing with flies")

ballroom = Room("Ballroom")
ballroom.set_description("A fancy ballroom")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A fancy dining hall")

# This links the kitchen to the dining hall
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dining_hall.set_character(dave)

dave.describe()

dave.set_conversation("Hi, my name is Dave. I'd like to eat your brain.")
dave.set_weakness("cheese")
dave.add_item("cheese")  # Adding item to enemy inventory

print("What will you fight with?")
fight_with = input("\n> ")

while dead == False:
    current_room = kitchen
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    print("Which direction would you like to go? North, east, south, west")
    command = input("\n> ").lower()  # Normalize input to lowercase
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Hooray, you won the fight!")
                current_room.set_character(None)
            else:
                print("Oh dear, you lost the fight.")
                dead = True  # End the game if you lose the fight
        else:
            print("There is no one here to fight with")
