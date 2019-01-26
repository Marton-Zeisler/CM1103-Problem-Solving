cars = ["bmw", "audi", "mercedes", "toyota"]
cars.sort(reverse=True)
print(cars)
print(sorted(cars)) # returns sorted, doesn't modify
cars.reverse()
print(cars)
print(list(reversed(cars)))
print(len(cars))

