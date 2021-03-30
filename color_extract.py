import colorgram

colors = colorgram.extract("hirst_real_artwork.jpg", 50)

color_rgb = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_rgb.append(new_color)

print(color_rgb)