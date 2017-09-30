# define a decorator
def logging_decorator(func):

    def carry(*args, **kwargs):
        print '[%s] is runing'%func.__name__

        return func(*args, **kwargs)
    return carry



# add a decorator to the function
@logging_decorator
def speak():
    print 'i am speaking'


## DEMO
if __name__ == '__main__':
    speak()