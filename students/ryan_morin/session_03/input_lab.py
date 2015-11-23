def input_lab():
    response = input('a prompt for a user >')
    if not response:
        input_lab()
    else:
        return response