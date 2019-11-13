"""email.py"""
import re


def valida(email):
    """valida

    :param email:
    """
    return re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$').match(
        email)
