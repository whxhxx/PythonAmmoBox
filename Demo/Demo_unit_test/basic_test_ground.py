import unittest

# import the testee
from my_math import *


class TestInstance(unittest.TestCase):
    """
    the test unit
    """


    # 1. basic functions for test
    def test_add(self):
        """
        the test functions MUST name started with "test"
        """
        expected = 6
        result = add(2,4)
        self.assertEqual(expected, result)

    def test_minus(self):
        expected = 2
        result = minus(5,4)
        self.assertEqual(expected, result)

    # 2. envir setup functions call every time
    def setUp(self):
        print ("do something befire test.Prepare envir")

    def tearDown(self):
        print ("do something after test.Clean up")

    # 3. envir setup functions call once
    @classmethod
    def setUpClass(cls):
        print("\nthis setUp only call once")

    @classmethod
    def tearDownClass(cls):
        print("\nthis tearDown only call once")




#------------------------------------------------

def main():
    unittest.main()
    pass

if __name__ == '__main__':
    main()
