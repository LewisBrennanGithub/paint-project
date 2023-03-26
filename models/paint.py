# class Paint:
    
#     def __init__ (self, name, description, initial_value, initial_offset_value, popularity = 0, id = None):
#         self.name = name
#         self.description = description
#         self.value = initial_value
#         self.offset_value = initial_offset_value
#         self.popularity = popularity
#         self.id = id

    # def update_value(self, new_value, new_offset_value):
    #     self.value = new_value
    #     self.offset_value = new_offset_value

class Paint:
    
    def __init__ (self, name, description, initial_value, popularity = 0, id = None):
        self.name = name
        self.description = description
        self.value = initial_value
        self.offset_value = self.invert_colour(initial_value.lstrip('#'))
        self.popularity = popularity
        self.id = id

    def invert_colour(self, hex_color):
        if self.offset_override == True:
            return hex_color
    # Convert hex color to RGB tuple
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2 ,4))  
    # Invert each color component using bitwise NOT operation
        inverted_rgb = tuple(~c & 0xff for c in rgb) 
    # Convert back to hex format
        inverted_hex = '{:02x}{:02x}{:02x}'.format(*inverted_rgb)
        return inverted_hex

        # self.update_override = False