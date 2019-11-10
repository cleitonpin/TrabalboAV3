"""data.py"""


def valida(data):
    """valida

    :param data:
    """
    return data.find('/') == 2 and len(data) == 10
