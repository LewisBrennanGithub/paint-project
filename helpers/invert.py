def invert_colour(hex_colour):
    # Check if input starts with "#"
    if hex_colour.startswith("#"):
        # Strip "#" character from input
        hex_colour = hex_colour[1:]
    # Convert hexadecimal color to RGB values
    rgb = tuple(int(hex_colour[i:i+2], 16) for i in (0, 2, 4))  
    # Invert RGB values
    inverted_rgb = tuple(~c & 0xff for c in rgb) 
    # Convert inverted RGB values to hexadecimal format
    inverted_hex = '{:02x}{:02x}{:02x}'.format(*inverted_rgb)
    # Prepend "#" character to inverted hexadecimal value
    return "#" + inverted_hex