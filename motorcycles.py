motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modifying
motorcycles[0] = 'ducati'
print(motorcycles)

# Add to the end
motorcycles.append('kawasaki')
print(motorcycles)

# Insert to anywhere
motorcycles.insert(0, 'honda')
print(motorcycles)

## Use these when you want to delete an item, and not use it again.
# Delete using position 
del motorcycles[1]
print(motorcycles)

# Delete using value
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nThis motorcycle - {too_expensive.title()} - was too expensive for me.\n")

## Use these when you want to delete an item, but use it again.
# Using pop() to remove the last item
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(f"The latest motorcycle I own is a {popped_motorcycle.title()}.")

# Using pop() to remove any item
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.\n")


### Making an dynamic list by creating a series of append() calls.
dynamic_mc = []

dynamic_mc.append('BMW R 1300 GS')
dynamic_mc.append('Honda NS750X')
dynamic_mc.append('Triumph Rocket 3 Storm')

print(dynamic_mc)

