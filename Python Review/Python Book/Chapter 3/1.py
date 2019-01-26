colors = ["red", "green", "blue"]
print(colors)
print(colors[-1])

colors.append("white")
colors.insert(1, "black")
print(colors)
del colors[0]
print(colors.pop(3)) # returns deleted item
print(colors)
colors.remove("black")
print(colors)
