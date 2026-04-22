bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# accessing elements in a list
print(bicycles[0])

# modifying elements in a list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# adding elements to a list
motorcycles.append('ducati')
print(motorcycles)

# inserting elements into a list
motorcycles.insert(0, 'freedom')
print(motorcycles)

# removing elements from a list
del motorcycles[4]
print(motorcycles)  

# Popping elements from a list
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)