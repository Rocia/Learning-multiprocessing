from multiprocessing import Process
import os

def details(title):
    print (title)
    print ('Module Name:', __name__)
    if hasattr(os, 'GetProcessID'):  # only available on Unix
        print ('parent process:', os.getppid())
    print ('process id:', os.getpid())

def A(name):
    details('Any Function A')
    print ('hello', name)

if __name__ == '__main__':
    details('main line')
    p = Process(target=A, args=('Alloy',))
    p.start()
    p.join()
'''
Output:-

main line
Module Name: __main__
process id: 3196
Any Function A
Module Name: __main__
process id: 5795
hello Alloy
'''