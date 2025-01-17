class Rectangle:
    def __init__(self, width=15, height=7):
        self.__width = width
        self.__height = height
        
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
new_retangle = Rectangle(5, 7)

print(new_retangle.get_width())