from pathlib import Path

path = Path('text_files/pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)
