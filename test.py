"""test_data.py"""
# -*- coding: utf-8 -*-

import unittest
from validador import data, usuario
from utils.senha import gerador


class TestValidaData(unittest.TestCase):
    """TestValidaData"""
    def test_should_return_(self):
        """should_return_an_valid_date"""

        valid_date = data.valida('19/19/1919')

        self.assertTrue(valid_date)

    def test_should_return_false(self):
        """test_should_return_false"""

        invalid_date = data.valida('19/19')

        self.assertFalse(invalid_date)


class TestValidaUsuarioo(unittest.TestCase):
    """TestValidaUsuarioo"""
    def test_should_return_false_when_user_size_larger_than_12(self):
        """test_should_return_true"""

        self.assertFalse(usuario.valida('foo'))

    def test_should_return_false_when_user_size_less_than_4(self):
        """test_should_return_false"""
        self.assertFalse(usuario.valida('asdfgqwerzxcva'))

    def test_should_return_true_when_user_size_larger_than_4_and_less_than_12(
            self):
        """
        test_should_return_true_when_user_size_larger_than_4_and_less_than_12
        """

        self.assertTrue(usuario.valida('asdfq'))


class TestValidaSenha(unittest.TestCase):
    """TestValidaSenha"""
    def test_should_return_password_hash(self):
        """test_should_return_password_hash"""

        senha_a = '74b87337454200d4d33f80c4663dc5e5'
        senha_b = '65ba841e01d6db7733e90a5b7f9e6f80'

        senha_a_valida = gerador.gera('aaaa')
        senha_b_valida = gerador.gera('bbbb')

        self.assertEqual(senha_a_valida, senha_a)
        self.assertEqual(senha_b_valida, senha_b)
