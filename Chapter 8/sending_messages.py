import sending_functions as sf     

message_list = [
    'hi and welcome',
    'how are you doing?',
    'do you have something interesting to show me?',
    'i am happy to see you.'
                ]

sent_messages = []

sf.show_messages(message_list)

sf.move_messages(message_list[:], sent_messages)

sf.show_messages(message_list)
sf.show_messages(sent_messages)