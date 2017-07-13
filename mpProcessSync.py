from multiprocessing import Process, Lock

def A(lockk, i):
    lockk.acquire()
    print ('Hello', i)
    lockk.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(15):
        Process(target=A, args=(lock, num)).start()

'''
Output:-

Hello 0
Hello 1
Hello 2
Hello 4
Hello 3
Hello 5
Hello 6
Hello 8
Hello 7
Hello 9
Hello 10
Hello 11
Hello 12
Hello 13
Hello 14
'''