food = ["burgers", "fries"]
herFood = food[:] # this makes a copy by value
hisFood = food # this makes a copy by reference
food.append("apples")
print(herFood)
print(hisFood)