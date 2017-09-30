class Error(Exception):
    def __init__(self, msg):
        print msg
    pass

class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

def mye(level):
    if level < 1:
        raise Exception("Invalid level", level)


if __name__ == '__main__':
    # try:
    #     raise Error('hello')
    #     print ' ----- '
    # except Error as error:
    #     pass

    # try:
    #     pass
    # except "Invalid level":
    #     print 1
    # else:
    #     print 2

    try:
        raise Networkerror("Bad hostname")
    except Networkerror as e:
        print 'im here waiting',e.args
