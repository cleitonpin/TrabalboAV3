"""usuario.py"""
# -*- coding: utf-8 -*-


def valida(usuario):
    """valida

    :param usuario:
    """
    return len(usuario) > 4 and len(usuario) < 12
