from item import *

class Character:
    # Creating a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.inventory = []  # Initialize inventory
        
    # Describing the character  
    def describe(self):
        print(self.name + " is here!")
        print(self.description)
        
    # Setting what this character will say when talked to​
    def set_conversation(self, conversation):
        self.conversation = conversation
        
    # Communication with the character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you.")
            
    # Fighting with the character
    def fight(self, combat_item):
        if combat_item is None:
            print("You must choose an item to fight with!")
            return False
        print(self.name + " doesn't want to fight with you")
        return True
    
    # Add item to inventory
    def add_item(self, item):
        self.inventory.append(item)
    
    def get_inventory(self):
        return self.inventory


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness
        
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item is None:
            print("You must choose an item to fight with!")
            return False
        if combat_item == self.weakness:
            print("You defeat " + self.name + " with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer.")
            return False
