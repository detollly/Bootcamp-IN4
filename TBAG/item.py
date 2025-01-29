class Item:
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_description(self):
        return self.description
    
    def set_description(self, item_description):
        self.description = item_description
        
    def describe_item(self):
        if self.description:
            print(self.description)
        else:
            print("This item has no description.")
