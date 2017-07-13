from multiprocessing import Process

def f(name):
    print ('Hi', name, '\nHave a nice day')

if __name__ == '__main__':
    p = Process(target=f, args=('Alloy',))
    p.start()
    p.join()

'''
Output:-

Hi Alloy 
Have a nice day
'''