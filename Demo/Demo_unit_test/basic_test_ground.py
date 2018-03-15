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



    condition = 1 < 100
    # SKIP decorator
    @unittest.skipIf( condition, "Wow I skipped it ")
    def test_minus(self):
        expected = 2
        result = minus(5,4)
        self.assertEqual(expected, result)

    def test_devide(self):
        # raise
        my_devidend = 2
        my_devisor = 0
        self.assertRaises(ZeroDivisionError, devide, my_devidend, my_devisor)


    # 2. envir setup functions call every time
    def setUp(self):
        print ("[ do something befire test.Prepare envir")

    def tearDown(self):
        print ("do something after test.Clean up ]")

    # 3. envir setup functions call once
    @classmethod
    def setUpClass(cls):
        print("\n- - this setUp only call once - -")

    @classmethod
    def tearDownClass(cls):
        print("\n- -this tearDown only call once - -")




#------------------------------------------------

def main():
    unittest.main()
    pass

if __name__ == '__main__':
    main()
