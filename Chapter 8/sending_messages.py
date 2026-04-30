def show_messages(message):
    '''Print a message from a list'''
    print(f"[This is the messages inside the list]:")
    for msg in message:
        print(msg)

def move_messages(sent):
    '''Moves from message_list to another list'''
    while sent:
        current_message = sent.pop()
        sent_messages.append(current_message)        

message_list = [
    'hi and welcome',
    'how are you doing?',
    'do you have something interesting to show me?',
    'i am happy to see you.'
                ]

sent_messages = []

show_messages(message_list)

move_messages(message_list[:])

show_messages(message_list)
show_messages(sent_messages)