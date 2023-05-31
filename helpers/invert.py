def invert_colour(hex_colour):
    if hex_colour.startswith("#"):
        hex_colour = hex_colour[1:]
    rgb = tuple(int(hex_colour[i:i+2], 16) for i in (0, 2, 4))  
    inverted_rgb = tuple(~c & 0xff for c in rgb) 
    inverted_hex = '{:02x}{:02x}{:02x}'.format(*inverted_rgb)
    return "#" + inverted_hex