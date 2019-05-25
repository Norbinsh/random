"""
Basic math tests.
"""

import program


class TestProgram:

    def test_add(self):
        assert 4 == program.add(2, 2)

    def test_substract(self):
        assert 2 == program.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == program.multiply(10, 10)
