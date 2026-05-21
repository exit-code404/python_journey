# Attempt on creating a separate json file storing a dictionary containing user info
from pathlib import Path
import json

def get_stored_userdata(path):
    """Retrieves the userdata if there is any"""
    if path.exists():
        contents = path.read_text()
        userdata = json.loads(contents)
        return userdata
    else:
        return None


def get_new_userdata(path):
    """Retrieves the username if there is any"""
    username = input("What should I call you? ")
    age = input("What is your age? ")
    location = input("What is your country? ")

    user_data = {
        "username": username,
        "age": age,
        "location": location
    }

    contents = json.dumps(user_data)
    path.write_text(contents)
    return user_data   

def greet_user():
    """Greets the User with stored info or creates new user."""
    path = Path("json_files/user001.json")
    user_data = get_stored_userdata(path)

    if user_data == None:
        user_data = get_new_userdata(path)
    else:
        is_correct = input(f"Is your name {user_data["username"]}? (yes/no) ")
        if is_correct == 'yes':
            prompt = f"Welcome back, {user_data["username"]}!"
            prompt += f"\nUser: {user_data["username"].title()}"
            prompt += f"\nAge: {user_data["age"]}"
            prompt += f"\nLocation: {user_data["location"].title()}"
            print(prompt)
        else:
            user_data = get_new_userdata(path)
            print(f"Your info have been saved, {user_data["username"]}.")

greet_user()                  

# How do I access the Dictionary content?