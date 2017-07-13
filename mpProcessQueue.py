from multiprocessing import Process, Queue

def A(queue,name):
    queue.put([12, None, 'Hi',name])

if __name__ == '__main__':
    queue = Queue()
    process = Process(target=A, args=(queue,'Alloy',))
    process.start()
    print (queue.get())
    process.join()


'''
Output:-

[12, None, 'Hi', 'Alloy']
'''