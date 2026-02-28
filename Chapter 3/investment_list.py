# List of items I need to prevent health issues later
in_list = ['Herman Miller Chair',
                    'Manduka Pro', 
                    'Manduka foam blocks', 
                    'Trigger Point foam roller', 
                    'Rouge Monster bands']

print(in_list)

print(f"\nThe {in_list[0]} costs around 15,000 NOK brand new. I might want to change that into a used instead.")
in_list[0] = 'Herman Miller Chair (Used)'
print(in_list)

print(f"\nUps I forgot to add the Yoga Straps into the list.")
in_list.append('Manduka Align Yoga Straps')
print(f"{in_list}\n")

# Removed foam blocks using .pop()
popped_items = in_list.pop(2)
print(f"{popped_items}\n")

# Inserted Cork Blocks
in_list.insert(2, 'Manduka Cork Block (x2)')

# Sort permanently
in_list.sort()
print(in_list)

# Length of the list
still_needed = len(in_list)

print(f"\nI still need to purchase {still_needed} items from my Investment List.")