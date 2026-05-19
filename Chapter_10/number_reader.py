from pathlib import Path
import json

path = Path('json_files/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)