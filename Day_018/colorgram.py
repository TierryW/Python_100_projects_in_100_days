import colorgram

rgb_colors = []
colors = colorgram.extract('C:/Users/willi/Downloads/Arquivos/Python_100_projects_in_100_days/Day_018/image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
