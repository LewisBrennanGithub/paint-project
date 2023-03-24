class Paint:
    
    def __init__ (self, name, description, initial_value, initial_offset_value, popularity = 0, id = None):
        self.name = name
        self.description = description
        self.value = initial_value
        self.offset_value = initial_offset_value
        self.popularity = popularity
        self.id = id

    def update_value(self, new_value, new_offset_value):
        self.value = new_value
        self.offset_value = new_offset_value
