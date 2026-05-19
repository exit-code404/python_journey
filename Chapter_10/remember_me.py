from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    """Prompt for a new username."""
    username = input("What's your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username    

def greet_user():
    """Greets the user by name"""
    path = Path('json_files/username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We will remember you next time, {username}")

try:
    greet_user()
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")        
