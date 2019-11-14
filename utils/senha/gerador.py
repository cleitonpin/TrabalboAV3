"""hash.py"""
# -*- coding: utf-8 -*-

import hashlib


def gera(senha):
    """gera

    :param senha:
    """

    return hashlib.md5(str(senha).encode('utf-8')).hexdigest()
