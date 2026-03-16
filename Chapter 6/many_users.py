users = {
    'secops': {
        'first': 'sec',
        'last': 'ops',
        'location': 'security operation',
    },

    'exitcode': {
        'first': 'exit',
        'last': 'code',
        'location': 'digital world',
    },

}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")