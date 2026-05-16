from pathlib import Path

path = Path('text_files/beyond_good_and_evil.txt')

contents = path.read_text()

print(contents.count('truth'))