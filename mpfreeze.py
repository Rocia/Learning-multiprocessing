from multiprocessing import Process, freeze_support

def A(name):
    print ('Hello',name,'!')

if __name__ == '__main__':
    freeze_support()
    Process(target=A, args=('Alloy',)).start()

'''
Output:-
 
Hello Alloy !
'''