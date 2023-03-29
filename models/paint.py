class Paint:
    
    def __init__ (self, name, description, initial_value, offset_value = "#000000", popularity = 0, id = None):
        self.name = name
        self.description = description
        self.value = initial_value
        self.offset_value = offset_value
        self.popularity = popularity
        self.id = id

    def decrease_popularity(self):
        self.popularity -= 1

    def increase_popularity(self):
        self.popularity += 1
