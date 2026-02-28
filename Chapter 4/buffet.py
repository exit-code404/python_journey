buffet = ('fish n chips', 'hamburger', 'meatballs', 'carbonara', 'meat stew')
print("Original menu:")
for food in buffet:
    print(f"\t - {food.title()}")

print("\nRevised menu:")
buffet = ('omelette', 
          'hamburger', 
          'meatballs', 
          'carbonara', 
          'salmon with dill sauce')
for food in buffet:
    print(f"\t - {food.title()}")
