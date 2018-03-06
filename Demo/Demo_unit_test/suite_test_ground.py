
import unittest
from basic_test_ground import TestInstance





def main():

    """
    part 1 : suite
    """
    suite = unittest.TestSuite()

    # 1 addTest() to add a single function to suite
    suite.addTest (TestInstance("test_add"))

    # 2 addTests() to add multiple functions to suite
    test_name_list = ["test_add", "test_minus"]
    test_list = [TestInstance(test_name_list[0]) , TestInstance(test_name_list[1])]
    suite.addTests(test_list)

    # 3 unittest.TestLoader()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestInstance))

    """
    part 2: runner
    """
    output_dir = 'C:\Users\dell\Documents\GitHub\PythonAmmoBox\Demo\Demo_unit_test\my_test_report.txt'
    with open(output_dir,'a') as file:
        runner = unittest.TextTestRunner(stream=file,verbosity=2)
        runner.run(suite)

    pass



#------------------------------------------

if __name__ == '__main__':
    main()
