def build_profile(first, last, **user_info):
    '''Build a dictionary containing everything we know about a user'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('dennis', 
                             'rodrigez', 
                             location='germany', 
                             field='software developer', 
                             education='cybersecurity analyst')

print(user_profile)

# Note: I might see parameter name **kwargs used to collect nonspecific keyword arguments.