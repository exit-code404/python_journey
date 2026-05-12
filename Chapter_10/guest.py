from pathlib import Path

guests = []

active = True
while active:
    
    name = input("Please enter your name: ")
    guests.append(name)

    path = Path('text_files/guest_list.txt')

    contents = "--- Guest list ---\n"
    for person in guests:
        contents += f"\t{person.title()}\n"
    path.write_text(contents)