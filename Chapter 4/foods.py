foods = ['italian pizza', 'protein pancakes', 'swedish meatballs']
friend_foods = foods[:]
foods.append('protein milkshake')
friend_foods.append('stew')

print("This is my favorite foods: ")
for food in foods:
    print(f"\t - {food.title()}")

print("\nThis is my friend's favorite foods: ")
for food in friend_foods:
    print(f"\t - {food.title()}")