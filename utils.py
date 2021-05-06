import string
import random


def generate_password(length: int = 10) -> str:

    chars = string.ascii_letters + string.digits
    password = ''

    for _ in range(length):
        password += random.choice(chars)

    return password


def generate_users(count: int = 100):
    users = []
    for index in range(count):
        users.append(index)

    return users


def foo():
    pass
