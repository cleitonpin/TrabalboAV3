"""test_data.py"""
# -*- coding: utf-8 -*-

import unittest
from validador import data


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
