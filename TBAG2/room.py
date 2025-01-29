class Room():
    def __init__(self, room_name):
        self.room_name = room_name
        self.description = None
        self.linked_rooms = {}
    
    def get_room_name(self):
        return self.room_name
    
    def set_description(self, room_name):
        self.name = room_name     
        
    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description
        
    
        
    def describe(self):
        print(self.description)
        