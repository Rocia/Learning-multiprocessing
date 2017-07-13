from multiprocessing import Process, Value, Array

def A(n, a):
    n.value = 3.14159269
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(15))

    p = Process(target=A, args=(num, arr))
    p.start()
    p.join()

    print (num.value)
    print (arr[:])
    
'''
OUTPUT:-

3.14159269
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14]
'''