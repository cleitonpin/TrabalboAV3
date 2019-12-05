"""email.py"""
import re


def valida(gmail):
    """valida

    :param email:
    """
    
    return gmail.find('@') == 1 and gmail.find('gmail.com') == 1
    #return re.compile(r'^[\w-] + @(?:[a-zA-Z0-9-] + \.) + [a-zA-Z]{2,}$')
