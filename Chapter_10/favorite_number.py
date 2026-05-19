from pathlib import Path
import json



path = Path('json_files/favorite_number.json')
if path.exists():
    content = path.read_text()
    print(f"I know your favorite number! It's {content}")
else:
    number = input("What's your favorite number? ")
    content = path.write_text(number)
    save_file = json.dumps(content)
    print("Your number has been saved!")


