usernames = ['admin', 'exitcode', 'codeblack', 'user404', 'secops']

if not usernames:
    print("There are currently no usernames in our database.")

for username in usernames:
    if username == 'admin':
        print(f"Hello {username.title()}, cup of coffee & a status report?")
    else:
        print(f"Hello {username}, it's great to have you back!")

