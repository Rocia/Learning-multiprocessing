from multiprocessing import Pool, TimeoutError
import time
import os

def A(x):
    return x**3

if __name__ == '__main__':
    pool = Pool(processes=4)              # start 4 worker processes

    print (pool.map(A, range(15)))

    # print same numbers in arbitrary order
    for i in pool.imap_unordered(A, range(10)):
        print (i)

    # evaluate "A(20)" asynchronously
    res = pool.apply_async(A, (20,))      # runs in *only* one process
    print (res.get(timeout=1))

    # evaluate "os.getpid()" asynchronously
    res = pool.apply_async(os.getpid, ()) # runs in *only* one process
    print (res.get(timeout=1))            # prints the PID of that process

    # launching multiple evaluations asynchronously *may* use more processes
    multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
    print ([res.get(timeout=1) for res in multiple_results])

    # make a single worker sleep for 10 secs
    res = pool.apply_async(time.sleep, (10,))
    try:
        print (res.get(timeout=1))
    except TimeoutError:
        print ("TIMEOUT WARNING! multiprocessing.TimeoutError")
        
'''
OUTPUT:-

[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]
0
1
8
27
64
125
216
343
512
729
8000
7382
[7380, 7381, 7380, 7381]
TIMEOUT WARNING! multiprocessing.TimeoutError
'''
