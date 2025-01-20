from character import Enemy
class Room:
    
    # constructor    
    def __init__(self):
        self.name = None
        self.description = None
        self.linked_rooms = {}
        self.character = None
        
        
    # creating getter and setter
    def get_description (self):
        return self.description
    
    def set_description(self, room_description):
        self.description = room_description
        
    def describe(self):
        print(self.description)
        
    def get_name(self):
        return self.name
    
    def set_name(self, room_name):
        self.name = room_name
        
    # linking rooms and navigating them
        
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        
    def get_details(self):
        print(self.name)
        print("------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
        print(f"The {room.get_name()} is {direction}")
        
    # movement function
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms
        else:
            print("You cannot go to that direction")
            return self
    