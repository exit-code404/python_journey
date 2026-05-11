from pathlib import Path

path = Path('text_files/python_learned.txt')

contents = path.read_text()

learned_list = []

for word in contents.splitlines():
    learned_list.append(word)

for line in learned_list:
    print(line)
