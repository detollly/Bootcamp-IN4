# Room class
class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None

    # Getter and setter for room name
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_description(self, room_description):
        self.description = room_description

    def describe(self):
        print(self.description)

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    # Linking rooms
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self.name)
        print("-------------------------")
        print(self.description)
        if not self.linked_rooms:
            print("There are no other rooms to go to.")
        else:
            for direction in self.linked_rooms:
                room = self.linked_rooms[direction]
                print(f"The {room.get_name()} is to the {direction}")

    # Movement function
    def move(self, direction):
        if direction in self.linked_rooms:
            print(f"You move to the {self.linked_rooms[direction].get_name()}.")
            return self.linked_rooms[direction]
        print("You cannot go to that direction.")
        return self
