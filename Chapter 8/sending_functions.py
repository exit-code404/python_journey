def show_messages(message):
    '''Print a message from a list'''
    print(f"[This is the messages inside the list]:")
    for msg in message:
        print(msg)

def move_messages(from_list, to_list):
    '''Moves from message_list to another list'''
    while from_list:
        current_message = from_list.pop()
        to_list.append(current_message)