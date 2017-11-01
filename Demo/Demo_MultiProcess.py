import multiprocessing
import time

def worker(target,gap):
    time.sleep(gap)
    print("i am",target)

    #     n -= 1


def main():
    a = multiprocessing.Process(target=worker, args=('jerry',2))
    b = multiprocessing.Process(target=worker, args=('tom',4))

    print ('done')
    a.start()
    b.start()

if __name__ == "__main__":
    main()



    # print "p.pid:", p.pid
    # print "p.name:", p.name
    # print "p.is_alive:", p.is_alive()
    # print "a.is_alive:", a.is_alive()
    # print "b.is_alive:", b.is_alive()
    # print "c.is_alive:", c.is_alive()
