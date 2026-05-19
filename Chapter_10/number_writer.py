from pathlib import Path
import json

numbers = [2, 4, 6, 8, 10, 12, 14]

path = Path('json_files/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)