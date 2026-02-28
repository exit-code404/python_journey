pizzas = ['margarita', 'mushroom and ham', 'pepperoni']

print("Favorite Pizzas:")
for pizza in pizzas:
    print(f"\tFavorite Pizza #{len(pizzas)}: {pizza.title()}")
print("\nA good pizza is always homemade!")

# As you can see, I tried - with my current knowledge - to make a dynamic list that updated the index numbers. However 
# I do not current attain that knowledge. There must be some sort of machanism that lets me choose the index number
# and then display that relative to the pizza in pizzas. 

friend_pizzas = pizzas[:]

pizzas.append('four cheese')
friend_pizzas.append('hawaii')

print("\nMy favorite pizzas are: ")
for pizza in pizzas:
    print(f"\t - {pizza.title()}")

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(f"\t - {pizza.title()}")    
             

