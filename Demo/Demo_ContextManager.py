"""
context manager demo
    To use 'with' statement to get resource and release resource, context manager helps
    it tp be simple and clear.
    1.context manager without importing the contextlib, __enter__ __exit__ are required;
    2.context manager with importing the contextlib.
"""

from contextlib import contextmanager

"""
1. context manager without the contextlib
"""
class GetFile(object):
    """ A self-defined context manager class """
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        """ will run this func when getting in the with statement """
        self.file_object = open(self.file_name, 'a')
        return self.file_object

    def __exit__(self, *args):
        """ will run this func when leaving the with statement """
        if self.file_object:
            self.file_object.close()



"""
2. context manager with the contextlib
"""
@contextmanager
def get_file_with_lib(file_name):
    """decorate the func with the @contextmanager and use the yield statement"""
    mode = 'a'
    try:
        open_data = open(file_name, mode)
        yield open_data
    finally:
        open_data.close()



#
#── FUNCTIONS FOR TEST ─────────────────────────────────────────────────────────
#


def test_without_lib(file_dir):
    """ TEST 1"""
    with GetFile(file_dir) as target_file:
        target_file.write('\nmethod1')

def test_with_lib(file_dir):
    """ TEST 2"""
    with get_file_with_lib(file_dir) as target_file:
        target_file.write('\nmethod2')


if __name__ == '__main__':
    FILE_DIR = 'C:\\Users\\dell\\Documents\\GitHub\\PythonAmmoBox\\data\\text.txt'

    test_without_lib(FILE_DIR)

    test_with_lib(FILE_DIR)
