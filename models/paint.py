class Paint:
    
    def __init__ (self, name, description, initial_value, offset_value = "#000000", popularity = 0, id = None):
        self.name = name
        self.description = description
        self.value = initial_value
<<<<<<< HEAD
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
=======
        self.offset_value = offset_value
        self.popularity = popularity
        self.id = id

    def decrease_popularity(self):
        self.popularity -= 1

    def increase_popularity(self):
        self.popularity += 1
>>>>>>> justincase
