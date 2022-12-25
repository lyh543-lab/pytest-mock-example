from os import getlogin


def get_greeting_string():
    user = getlogin()
    return f'Greetings, {user}'
