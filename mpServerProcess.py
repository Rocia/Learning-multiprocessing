from multiprocessing import Process, Manager

def A(d, l):
    d[1] = '2'
    d['2'] = 3
    d[3.14] = None
    d['alpha'] = None
    d['beta'] = 'gamma'
    l.reverse()

if __name__ == '__main__':
    manager = Manager()

    DICTIONARY = manager.dict()
    LIST = manager.list(range(15))

    process = Process(target=A, args=(DICTIONARY,LIST))
    process.start()
    process.join()

    print (DICTIONARY)
    print (LIST)
    
'''
OUTPUT:-

{1: '2', '2': 3, 3.14: None, 'alpha': None, 'beta': 'gamma'}
[14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
'''