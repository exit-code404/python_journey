from user_role import User
from admin_role import Admin

user001 = User('Daniel', 'B.', 'Oslo', 'Digital Analyst')
user002 = User('Anna', 'P.', 'Skjetten', 'Lab Researcher')
user003 = User('Emilie', 'W.', 'Lillestrøm', 'Restaurant Waiter')

users = [user001, user002, user003]

for user in users:
    user.greet_user()
    user.describe_user()
    user.privileges.show_privileges()

admin001 = Admin('Rob', 'P.', 'Bergen', 'Digital Administrator')
admin001.describe_user()
admin001.privileges.show_privileges()    