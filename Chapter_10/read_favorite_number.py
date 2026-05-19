from pathlib import Path
import json

path = Path("json_files/favorite_number.json")

content = path.read_text()

print(f"I know your favorite number! It's {content}")