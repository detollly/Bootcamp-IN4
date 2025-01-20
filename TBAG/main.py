from room import Room
from character import Enemy

kitchen = Room()
kitchen.set_name("kitchen")
kitchen.set_description("A dark and dirty room buzzing with flies")

ballroom = Room()
ballroom.set_name("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")

dining_hall = Room()
dining_hall.set_name("dining_hall")
dining_hall.set_description("A large room with ornate golden decorations")

dave = Enemy()

dining_hall.set_character(dave)

# directions
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")

dining_hall.get_details()

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(dining_hall, "east")
ballroom.link_room(ballroom, "east")

current_room = kitchen

while True:
  print("\n")
  current_room.get_details()

  inhabitant = current_room.get_character()
  if inhabitant is not None:
      inhabitant.describe()

      command = input("> ")
      current_room = current_room.move(command)