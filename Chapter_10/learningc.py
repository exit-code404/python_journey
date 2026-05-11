from pathlib import Path

path = Path('text_files/python_learned.txt')

contents = path.read_text()

message = contents.replace('python', 'ruby')

print(message)