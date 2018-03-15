"""
[Python3 basic libs demo]
"""



"""
[os]
"""
def demo_os():
    import os
    #get current work direction
    cur_wd = os.getcwd()

    #change current work direction
    dir_str = ""
    new_wd = os.chdir(dir_str)

    # execute system command
    command = ""
    os.system(command)

"""
[shutil]
more functions for files operations
"""
def demo_shutil():
    import shutil
    data_src = ""
    data_dst = ""
    #copy
    shutil.copyfile(src=data_src,dst=data_dst)
    #move
    shutil.move(src=data_src,dst=data_dst)
    #archive
    shutil.make_archive(base_name="the name of file", format="zip/tar/..", root_dir="dir to be archived" )


"""
[glob]
search all matching files
"""
def demo_glob():
    import glob
    #search all .jpgs
    print glob.glob(r"E:/Picture/*/*.jpg")
    #search all py files
    print glob.glob(r'../*.py') #relative dir

def demo_glob_iter():
    """
    return a iterator of results
    """
    import glob
    #get a result iterator
    file_iter = glob.iglob(r'../*.py')
    print file_iter #<generator object iglob at 0x00B9FF80>

    for file in file_iter:
        print file

"""
[sys.argv]
"""
import sys
def sys_argv_demo():
    """
    return: list
    """
    print "system arguments:",(sys.argv)

    """
    [stdin, stdout, stderr]
    """
    sys.stdin.read()
    sys.stdout.write()
    sys.stderr.write()




"""
[TEST]
"""
if __name__ == '__main__':
    sys_argv_demo()
    pass


