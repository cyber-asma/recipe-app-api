"""
simple test
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test for calc app"""
    def test_add(self):
        """Test add function"""
        self.assertEqual(calc.add(3, 8), 11)

    def test_subtract(self):
        """Test subtract function"""
        self.assertEqual(calc.subtract(11, 5), 6)
