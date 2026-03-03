current_users = ['admin', 'Exitcode', 'codeblack', 'user404', 'secops']

new_users = ['blackheart', 'hollowcode', 'exitcode', 'SECOPS', 'tiredtear']

for new_user in new_users:
    current_user = [current_user.lower() for current_user in current_users]
    new_user = new_user.lower()
    if new_user in current_user:
        print(f"{new_user} - This username is not available. Please choose another.")
    else:
        print(f"{new_user} - This username is available!")