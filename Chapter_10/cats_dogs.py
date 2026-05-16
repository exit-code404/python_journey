from pathlib import Path

filenames = ['text_files/cats.txt', 'text_files/dogs.txt', 'text_files/birds.txt']

for filename in filenames:
    path = Path(filename)
    try:
        content = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(content)