class Room:
    
    # constructor    
    def __init__(self):
        self.name = None
        self.description = None
        self.linked_rooms = {}
        
        
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
        self.linked_room[direction] = room_to_link
        
    def get_details(self):
        print(self.name)
        print("------------")
        print(self.description)
        for direction in self.linked_room:
            room = self.linked_rooms[direction]
        print("The " + room.get_name()+ " is " + direction)
    