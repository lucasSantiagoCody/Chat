def error_message_handler(messages_error:list):
    single_message = ""

    for msg_error in messages_error:
        single_message += f"{msg_error}, "

    # to return single msg and dont show last comma
    return single_message[:len(single_message.rstrip())-1]
