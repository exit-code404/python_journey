guest_list = ['my father', 'my fathers parents', 'my fathers unknown daugther']

print("Invitations round #1:\n")
message_father = f"{guest_list[0]} - I hereby invite you to a family union dinner. I want to meet you father. 20.00 PM next saturday."
print(message_father)

message = f"{guest_list[1]} - I hereby invite you to a family union dinner. We will be at my place next week on saturday."
print(message)

message_sister = f"{guest_list[2]} - I hereby invite you to a family union dinner. I heard I have got a sister. I can't wait to meet you!"
print(message_sister)

# Changing guest list
print(f"\n{guest_list[1]}, seem to not be able to make it to dinner unfortuneately.")

guest_list[1] = 'my mother'
message_mother = f"{guest_list[1]} - I would love to reunite our original family for a nice dinner next Saturday at my place."

print("\nInvitation round #2:\n")
print(message_father)
print(message_sister)
print(message_mother)

# More guests
print("\nI have an announcement to make! I have officially found a much bigger table, so more guests will come.\n")

guest_list.append('my uncle')
guest_list.insert(3, 'my grandmother')
guest_list.insert(3, 'my aunt')

print("Invitation Round #3:\n")
print(message_father)
print(message_sister)
print(message_mother)
message = f"{guest_list[3]} - I would love for you to meet my father at family reunion dinner at my place."
print(message)
message = f"{guest_list[4]} - I would love for you to meet my father at family reunion dinner at my place."
print(message)
message = f"{guest_list[-1]} - I would like for you to meet my father at family reunion dinner at my place."
print(message)

# Shrinking Guest list

print("\nI am very sad to announce that I will only be able to have two guests over this saturday.")

popped_guests = guest_list.pop()
print(f"\n{popped_guests} I am very sad to inform you that your invitation to the family reunion have been cancelled")

popped_guests = guest_list.pop()
print(f"{popped_guests} I am very sad to inform you that your invitation to the family reunion have been cancelled")

popped_guests = guest_list.pop()
print(f"{popped_guests} I am very sad to inform you that your invitation to the family reunion have been cancelled")

popped_guests = guest_list.pop()
print(f"{popped_guests} I am very sad to inform you that your invitation to the family reunion have been cancelled")

print(f"\n{guest_list[0]} and {guest_list[1]} - Both of you are still invited. I would love for this little reunion to happen.")

del guest_list[0]
del guest_list[0]
print(guest_list)

# Exercise 3-9
print(len(guest_list))