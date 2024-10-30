import colorgram

RGBcolours = []
colours = colorgram.extract('HirstPainting.jpg', 30)

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    newColour = (r, g, b)
    RGBcolours.append(newColour)

print(RGBcolours)

