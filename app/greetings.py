import os
from os import getlogin

from lib.utils import HostUtils


def get_greeting_string_from_import_function():
    user = getlogin()
    return f'Greetings, {user}'


def get_greeting_string_from_import_module():
    user = os.getlogin()
    return f'Greetings, {user}'


def get_greeting_string_from_import_class_method():
    host_utils = HostUtils()
    user = host_utils.get_username()
    return f'Greetings, {user}'
