from contextlib import contextmanager


@contextmanager
def make_open_context(filename, mode):
    fp = open(filename, mode)
    try:
        yield fp
    finally:
        fp.close()



with make_open_context('./data/text12.txt','a') as f:
    f.write('hello world')


